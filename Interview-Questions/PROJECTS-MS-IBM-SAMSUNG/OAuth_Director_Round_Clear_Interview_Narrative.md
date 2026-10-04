# OAuth Migration - Director Round Interview Narrative

## Goal of the discussion

The main message is:

> I led a security-critical migration in SDX from legacy MSA v1 (RPS)
> authentication to MSA v2 (OAuth 2.0). The difficult part was not
> generating OAuth tokens. The difficult part was making those tokens
> trustworthy inside a .NET Framework-based SDX application by correctly
> integrating MISE validation and decryption, preserving a common
> session model for Windows and web scenarios, running RPS and OAuth
> together during migration, and completing the rollout without security
> or partner regressions.

This is the story to communicate in the first 15-20 minutes. The
remaining discussion can go deeper into MISE, ESTS, session management,
latency, reliability, throughput, scalability, security and rollout.

------------------------------------------------------------------------

# 1. Problem Statement and My Ownership

SDX was using the legacy MSA v1 RPS authentication model. We needed to
migrate the application to MSA v2 OAuth 2.0.

This was not simply a change from one authentication API to another.
Authentication was part of the trust boundary of SDX. A token being
generated successfully did not mean that SDX could trust it. The token
had to be validated and, where required, decrypted correctly before SDX
could construct an authenticated user identity.

My work covered the OAuth authentication path end-to-end:

-   understanding how OAuth tokens were generated through ESTS;
-   integrating MISE into the .NET Framework-based SDX application;
-   validating and decrypting the access token;
-   extracting trusted claims;
-   rebuilding `OAuthIdentity` and `UserSession.Current`;
-   supporting both Windows/CXH and web authentication scenarios;
-   supporting RPS and OAuth simultaneously during migration;
-   using flighting for controlled rollout;
-   protecting existing partner scenarios from regression;
-   ensuring that the new authentication path complied with Microsoft's
    token-validation/security requirements.

The project therefore had four important migration outcomes:

1.  No security/SFI regression.
2.  RPS and OAuth could coexist during transition.
3.  RPS could be removed gradually rather than through a big-bang
    cutover.
4.  Existing partner scenarios continued working without regression.

------------------------------------------------------------------------

# 2. Architecture

There were two major token-acquisition paths, but both converged on the
same validation and identity model.

## Windows / CXH flow

``` text
Windows / CXH
     |
     | PostTicket / TOKEN_BROKER
     v
    ESTS
     |
     | access_token + id_token
     v
    SDX
     |
     | Bearer access_token
     v
    MISE
     |
     | Validate signature / issuer / audience
     | Perform required key discovery
     | Decrypt token / expose trusted claims
     v
 OAuthIdentity
     |
     v
 UserSession.Current
     |
     v
 Existing SDX / partner scenario
```

## Web flow

``` text
Browser
   |
   | Redirect to ESTS authorization endpoint
   v
 ESTS
   |
   | Authorization code
   v
 SDX OAuth callback
   |
   | Exchange code for tokens
   v
 MISE validation / decryption
   |
   v
 OAuthIdentity
   |
   v
 UserSession.Current
```

The key architectural principle was:

> Token acquisition could be different for Windows and web, but the
> trust decision and application identity model should converge. Both
> scenarios ultimately relied on MISE-backed validation and the same SDX
> identity/session abstraction.

ESTS was responsible for authenticating the user and issuing OAuth
tokens. MISE was responsible for validating and decrypting the access
token and exposing trusted claims to SDX.

------------------------------------------------------------------------

# 3. Biggest Technical Challenge - MISE Integration

The biggest challenge was making MISE validation and decryption work
correctly inside SDX.

SDX was based on .NET Framework. For our scenario, MISE integration was
not a straightforward plug-and-play path with abundant examples and
documentation. I had to understand the integration from first
principles.

The difficult areas were:

### MISE initialization and configuration

I had to understand how MISE was initialized and which configuration
values were required for the application and environment. A token could
be perfectly valid at the issuer side, but incorrect application
configuration could still cause validation to fail.

### ESTS and MISE responsibilities

I needed a clear mental model of the trust chain:

``` text
ESTS = authenticate user + issue token
MISE = validate token + decrypt token + expose trusted claims
SDX  = build application identity/session from trusted claims
```

This distinction became essential while debugging because token
generation success only proved that the issuance side worked. It did not
prove that SDX could safely consume the token.

### First-party application behavior

I had to understand how the SDX first-party application configuration
interacted with token issuance and validation, including
client/application configuration and the expectations of the validation
path.

### Encrypted token claims

Some information required by SDX could come through the MISE-decrypted
access token. Therefore, simply parsing a JWT was not an acceptable
replacement for proper MISE validation and decryption.

### Limited directly applicable guidance

Generic OAuth knowledge was useful, but the difficult part involved
internal MISE/SDX behavior and environment-specific configuration. AI
tools could help with general reasoning and code exploration, but they
could not resolve the internal integration details for me.

I therefore used controlled experimentation:

1.  Understand the expected token flow.
2.  Verify MISE initialization.
3.  Verify environment and application configuration.
4.  Generate the OAuth token.
5.  Pass the access token to MISE.
6.  Inspect the validation result and failure information.
7.  Verify decrypted claims.
8.  Build `OAuthIdentity`.
9.  Rebuild `UserSession.Current`.
10. Test the complete scenario in PPE.
11. Use telemetry to correlate failures with the relevant authentication
    stage.
12. Repeat until the complete trust chain was working.

The important engineering point is that I did not stop when token
generation started working. I traced the authentication flow until SDX
could safely consume the token and establish the expected user session.

### How I would summarize this challenge

> The hardest part of the migration was the MISE integration. SDX was a
> .NET Framework application and there was limited directly applicable
> support for our scenario. I had to understand MISE initialization,
> configuration, ESTS interaction, first-party application behavior,
> token validation, decryption and claims handling from the ground up. I
> used code tracing, PPE testing, telemetry and controlled experiments
> to isolate issues. Once I understood the trust chain, I converted that
> learning into a reusable MISE validation path instead of solving each
> feature independently.

------------------------------------------------------------------------

# 4. Most Critical Problem Resolved - Establishing the Correct Security Boundary

The most critical problem was ensuring that SDX never treated successful
OAuth token generation as successful authentication.

The real security boundary was:

``` text
Token generated
      |
      v
MISE validation succeeds
      |
      v
Token is decrypted
      |
      v
Trusted claims are obtained
      |
      v
OAuthIdentity is created
      |
      v
Authenticated SDX session
```

Microsoft had strict token-validation requirements. In our environment,
incorrect or non-compliant validation could become an SFI/security
finding and come with a strict remediation deadline.

Therefore, the migration had to ensure that a token was trusted only
after the required MISE validation/decryption path succeeded.

The message to communicate is:

> OAuth token generation proved that the new issuance flow worked. MISE
> validation proved that SDX could trust the token. My most critical
> responsibility was closing that gap correctly so the migration did not
> introduce a security vulnerability or SFI risk.

------------------------------------------------------------------------

# 5. Second Major Challenge - Common Session Handling for Windows and Web

The next major challenge was session management.

Windows/CXH and browser scenarios obtained tokens differently:

-   Windows/CXH used PostTicket / TOKEN_BROKER.
-   Web scenarios used the authorization-code flow and authentication
    cookies.

If each flow created its own authentication/session implementation, SDX
would have ended up with two different identity models.

Instead, both flows converged on the same validation and session model.

For the web/cookie path, `OAuthAuthenticationModule` participated in
`AuthenticateRequest`, obtained the access token, invoked MISE
validation/decryption and rebuilt the SDX session.

For the PostTicket path, the received tokens were passed through
`ReauthenticateWithMiseToken`, which performed the same logical
validation and rebuilt the same `OAuthIdentity` / `UserSession.Current`.

`MiseHandlerService` provided a reusable MISE handler within the SDX
process. It was initialized once and reused by the authentication paths.

The architectural message is:

> Windows and web had different ways of acquiring tokens, but I kept
> token validation and application identity consistent. Both paths
> converged on MISE and ultimately produced the same SDX session
> abstraction. That prevented authentication details from leaking into
> every partner feature.

------------------------------------------------------------------------

# 6. Migration Strategy

The migration had four explicit guardrails.

## 6.1 No security / SFI regression

The new OAuth path had to satisfy the required token-validation model.
SDX could not establish a trusted identity merely because it had
received an OAuth token.

Security correctness took priority over making the new path appear
successful.

## 6.2 Dual authentication - RPS + OAuth

RPS and OAuth needed to coexist during migration.

Conditional authorization allowed SDX to select the appropriate
authentication model based on the request/token/flight state.

This was important because the entire application and all partner
scenarios could not be migrated atomically.

## 6.3 Gradual RPS removal

OAuth was flight gated by scenario.

That allowed the migration to proceed incrementally:

``` text
RPS only
   |
   v
RPS + OAuth coexistence
   |
   v
OAuth enabled for controlled scenarios
   |
   v
Increase OAuth adoption
   |
   v
Validate health and partner behavior
   |
   v
Gradually remove RPS dependency
```

The main advantage was blast-radius control. A problem in one OAuth
scenario did not require treating the entire application as a single
big-bang migration.

## 6.4 No partner regression

Existing SDX partners depended on identity and device information
exposed through the session.

The authentication mechanism underneath could change, but the downstream
application behavior had to remain stable.

The new OAuth identity therefore needed to expose the trusted claims
expected by existing scenarios, such as user and device identifiers.

The partner contract was effectively:

``` text
Old authentication implementation
              |
              v
       Expected SDX identity
              |
       migration happens
              |
              v
       Expected SDX identity
              |
              v
 Existing partner behavior continues
```

This is an important Principal-level point: the migration changed
authentication infrastructure while minimizing the amount of change
visible to consumers.

------------------------------------------------------------------------

# 7. Reliability

For this project, reliability meant:

> A legitimate authentication request should consistently reach the
> correct authenticated outcome, while failures should be controlled,
> observable and should never accidentally create a trusted identity.

Important reliability signals included:

-   MISE initialization health;
-   token-validation success/failure;
-   authentication exceptions;
-   missing or invalid token behavior;
-   scenario/partner success;
-   health of external authentication dependencies;
-   regression between the legacy and OAuth paths during rollout.

Flighting was also a reliability mechanism because it controlled blast
radius.

The migration was therefore not just:

``` text
Does the service process run?
```

It was:

``` text
Can the user authenticate correctly?
        +
Is the token trusted correctly?
        +
Does the partner scenario continue working?
        +
Does failure remain controlled?
```

------------------------------------------------------------------------

# 8. Latency

Authentication was on the request path, so latency needed to be
understood at both end-to-end and component levels.

A useful latency breakdown is:

``` text
OAuth end-to-end latency
       |
       +-- Token acquisition / ESTS
       |
       +-- MISE validation
       |
       +-- Key-discovery impact when required
       |
       +-- Token decryption / claims processing
       |
       +-- OAuthIdentity / UserSession construction
       |
       +-- Subsequent scenario work
```

The important percentiles are:

-   **p50** - typical request experience;
-   **p90** - slower portion of traffic;
-   **p99** - tail latency;
-   **p99.9** - extreme tail.

For authentication, p99 is particularly useful because average latency
can look healthy even when a smaller population of users is experiencing
very slow authentication.

If p50 remained stable but p99 increased, I would isolate the stages and
check:

1.  ESTS/token-acquisition latency.
2.  MISE validation latency.
3.  Key-discovery behavior.
4.  Network/dependency delays.
5.  Timeouts.
6.  Resource contention.
7.  Whether the issue was limited to a specific scenario, environment or
    flight.

During migration, the most useful comparison was the behavior of the new
OAuth path against the existing RPS path while both were available.

------------------------------------------------------------------------

# 9. Throughput

Throughput means the amount of authentication/request work handled per
unit time.

The important observation in this design is that authentication work was
not limited to the initial login. In the web/cookie path,
`OAuthAuthenticationModule` participated in `AuthenticateRequest` and
could invoke MISE validation before rebuilding the session.

Therefore:

``` text
Authenticated request volume increases
              |
              v
MISE validation work increases
              |
              v
CPU / network / dependency pressure can increase
              |
              v
Latency and failure rate must be monitored
```

The throughput discussion should therefore focus on:

-   request volume;
-   MISE validation volume;
-   validation latency;
-   error/timeout rate;
-   resource utilization;
-   dependency health.

------------------------------------------------------------------------

# 10. Scalability

Scalability means:

> As authentication/request volume increases, can the OAuth path
> continue meeting its latency, reliability and security requirements?

One useful design characteristic was that `MiseHandlerService` was
initialized once per SDX process and reused instead of reconstructing
the MISE handler for every request.

Scalability validation would focus on:

-   representative load testing;
-   authentication throughput;
-   p50/p90/p99 latency under load;
-   MISE validation latency;
-   timeout/error growth;
-   CPU/memory/thread pressure;
-   dependency behavior;
-   whether partner scenarios remain healthy as load increases.

The key relationship is:

``` text
Traffic increases
      |
      v
Validation work increases
      |
      v
Resource/dependency pressure increases
      |
      v
Tail latency may increase
      |
      v
Timeouts may increase
      |
      v
Authentication success rate can decrease
      |
      v
Reliability is affected
```

This connects throughput, scalability, latency and reliability rather
than treating them as unrelated concepts.

------------------------------------------------------------------------

# 11. Availability and Critical Dependencies

The OAuth flow depended on multiple critical components.

``` text
Client
  |
  v
Token acquisition
  |
  v
ESTS
  |
  v
SDX
  |
  v
MISE validation/decryption
  |
  v
Authenticated session
```

ESTS was critical for token issuance.

MISE was critical for validating/decrypting the token before SDX trusted
the identity.

From the SDX perspective, failure or severe latency in these
dependencies could affect authentication availability.

The important security decision was that availability could not be
improved by simply trusting an unvalidated token.

For protected authentication:

> If token validation cannot establish trust, SDX should not create a
> trusted authenticated identity. Authentication security cannot be
> bypassed just to keep the user flow available.

This is the security-versus-availability trade-off I would explain in a
Director discussion.

------------------------------------------------------------------------

# 12. Observability

Observability was essential because this migration crossed several
components.

The authentication flow needed enough telemetry to answer:

``` text
Did token acquisition succeed?
        |
Did MISE initialize correctly?
        |
Did token validation succeed?
        |
Did decryption return the required claims?
        |
Was OAuthIdentity created correctly?
        |
Was UserSession rebuilt correctly?
        |
Did the partner scenario complete?
```

Useful dimensions for investigation include:

-   authentication mode: RPS / OAuth;
-   scenario or flight;
-   MISE validation result;
-   failure category;
-   environment;
-   partner flow;
-   latency stage;
-   dependency health.

This allowed a rollout problem to be localized instead of treating every
authentication failure as the same issue.

------------------------------------------------------------------------

# 13. Director-Level Story: Biggest Challenge

If asked, **"What was the biggest challenge you faced?"**, I would
answer:

> The biggest challenge was getting MISE token validation and decryption
> working correctly in the .NET Framework-based SDX application. Token
> generation through OAuth was comparatively straightforward, but SDX
> could not trust that token until the server-side validation path was
> correct. There was limited directly applicable guidance for our MISE
> integration, so I had to understand the system from first principles -
> MISE initialization and configuration, ESTS token issuance,
> first-party application behavior, signing-key discovery, encrypted
> claims and the validation result.
>
> I approached it as a structured debugging problem. I separated token
> issuance from validation, verified configuration, traced the token
> into MISE, inspected failures and claims, tested repeatedly in PPE and
> used telemetry to validate each stage. AI tools were useful for
> generic concepts but not enough for the internal integration details,
> so the solution came from understanding the actual system behavior.
>
> Once I had the flow working, I made it reusable rather than
> feature-specific. Both Windows and web authentication paths converged
> on the same MISE-backed identity and session model. That was important
> because the migration also had to satisfy strict security
> requirements, support RPS and OAuth simultaneously, allow gradual RPS
> removal and avoid regression for partner teams.

------------------------------------------------------------------------

# 14. Director-Level Story: Most Critical Problem Resolved

If asked, **"What was the most critical problem you solved?"**, I would
answer:

> The most critical problem was closing the gap between token generation
> and token trust. SDX could successfully receive an OAuth token, but
> that alone was not sufficient. Under Microsoft's security
> requirements, the token had to be correctly validated and decrypted
> through MISE before SDX could construct an authenticated identity.
>
> If that validation path was implemented incorrectly, it was not simply
> a functional bug; it could become a security/SFI issue with a strict
> remediation timeline. I therefore treated successful MISE validation
> as the authentication trust boundary.
>
> I resolved the MISE integration, made the validation path reusable,
> and connected the validated claims to the existing SDX session model.
> That allowed us to move toward OAuth without weakening token
> validation or forcing partner applications to redesign their identity
> consumption.

------------------------------------------------------------------------

# 15. Director-Level Story: Session Challenge

If asked, **"What was the second hardest problem?"**, I would answer:

> The second challenge was session consistency between Windows and web
> scenarios. Windows/CXH acquired tokens through
> PostTicket/TOKEN_BROKER, while web scenarios used an
> authorization-code/cookie flow. I did not want these to become two
> independent authentication implementations.
>
> I made the acquisition mechanism an implementation detail. Both flows
> converged on MISE for validation/decryption and then constructed the
> same OAuthIdentity/UserSession model. The reusable MISE handler was
> initialized once within the SDX process and used by the authentication
> paths. This allowed downstream partner code to consume a consistent
> identity regardless of how the OAuth token was acquired.

------------------------------------------------------------------------

# 16. Cross-Questions to Expect

## Why was this migration difficult if OAuth is a standard protocol?

OAuth itself was not the difficult part. The difficult part was
integrating the new trust model into an existing .NET Framework
application with existing session semantics and partner dependencies.
Token issuance, MISE validation/decryption, encrypted claims,
application configuration and backward compatibility all had to work
together.

## Why was token generation not enough?

Because possession of a token does not establish that SDX should trust
it. The token still needed the required validation of signature, issuer
and audience and the required decryption/claims processing before an
authenticated SDX identity could be created.

## Why was MISE needed?

MISE provided the required server-side token-validation/decryption path
and returned trusted authentication information/claims to SDX.

## What happens if MISE validation fails?

The authentication flow does not establish a trusted OAuth identity. The
failure is observed/logged and the scenario follows its controlled
failure behavior.

## Why not simply decode the JWT?

Decoding is not equivalent to validating trust. The design required MISE
validation and included encrypted access-token claims. SDX needed the
trusted result of the validation/decryption path.

## How did you support RPS and OAuth together?

Conditional authorization and flighting allowed the application to
select the appropriate authentication path during migration. This
allowed OAuth to be introduced gradually while existing RPS scenarios
remained operational.

## How did you remove RPS safely?

The migration was scenario/flight controlled. OAuth could be enabled
progressively, health and partner behavior could be validated, and RPS
dependency could then be reduced gradually.

## How did you prevent partner regression?

The new OAuth path rebuilt the SDX identity/session using trusted claims
so existing downstream scenarios continued to receive the
identity/device information they depended on. Partner scenarios were
validated as OAuth adoption increased.

## What did AI contribute?

AI was useful for general OAuth concepts, code navigation and hypothesis
generation. The hard problems involved internal MISE behavior and
environment-specific configuration, which required direct code tracing,
telemetry, PPE testing and experimentation.

## How would you investigate high p99?

Break the authentication path into stages and determine whether the tail
is coming from token acquisition, MISE validation, key discovery,
network/dependency latency, timeouts or resource contention. Then
correlate the latency increase with validation/error rates and the
affected scenario/flight.

## What does reliability mean here?

Correct authentication outcome over time: legitimate users authenticate
successfully, invalid/unvalidated tokens never become trusted
identities, failures are controlled, and partner scenarios remain
healthy.

## What does scalability mean here?

As request and validation volume grows, the OAuth path should continue
meeting latency, reliability and security requirements without
validation becoming a bottleneck.

## What are the critical dependencies?

ESTS for token issuance and MISE for the required validation/decryption
path are critical dependencies from SDX's perspective.

## Would you fail open if MISE became unavailable?

For a protected authentication decision, I would not create a trusted
identity from an unvalidated token. That would exchange an availability
incident for a security vulnerability.

------------------------------------------------------------------------

# 17. 15-20 Minute Speaking Plan

  -----------------------------------------------------------------------
  Time                                What to communicate
  ----------------------------------- -----------------------------------
  0-2 min                             RPS to OAuth problem,
                                      security-critical nature, your
                                      ownership and four migration
                                      outcomes

  2-5 min                             Draw Windows/CXH + web acquisition
                                      paths, ESTS, SDX, MISE and common
                                      session model

  5-9 min                             Biggest challenge: MISE integration
                                      in .NET Framework, limited direct
                                      guidance, learning
                                      internals/configuration/ESTS

  9-12 min                            Session challenge: Windows and web
                                      converge on the same MISE-backed
                                      OAuthIdentity/UserSession

  12-16 min                           Reliability, latency, throughput,
                                      scalability and critical
                                      dependencies tied to the real
                                      authentication path

  16-19 min                           No SFI/security regression, dual
                                      auth, gradual RPS removal and no
                                      partner regression

  19-20 min                           Outcome, engineering lessons and
                                      Principal-level ownership
  -----------------------------------------------------------------------

------------------------------------------------------------------------

# 18. Final 60-Second Summary

> I would summarize the project as a security and reliability migration
> rather than simply an OAuth implementation. The new token-acquisition
> path was only the starting point. The critical engineering work was
> making the token trustworthy inside SDX through correct MISE
> validation and decryption.
>
> I had to understand MISE, ESTS, first-party configuration and
> encrypted claims from the ground up because the .NET Framework
> integration for our scenario was not straightforward. I then made the
> result reusable so Windows and web flows could converge on the same
> authenticated session model.
>
> The migration was designed around four outcomes: no security/SFI
> regression, RPS and OAuth coexistence during transition, gradual RPS
> removal, and no partner regression. Operationally, I think about the
> solution through authentication reliability, p99 latency, validation
> throughput, scalability under increased load and dependency failure
> behavior.
>
> The key result was that we moved the authentication trust boundary to
> OAuth/MISE without forcing a risky big-bang change on the rest of SDX
> or its partner scenarios.
