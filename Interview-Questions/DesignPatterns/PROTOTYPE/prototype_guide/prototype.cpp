#include <iostream>
#include <map>
#include <memory>
#include <stdexcept>
#include <string>
using namespace std;

class Notification {
public:
    virtual ~Notification() {}
    virtual unique_ptr<Notification> clone() const = 0;
    virtual void setRecipient(const string& recipient) = 0;
    virtual void setMessage(const string& message) = 0;
    virtual void send() const = 0;
};

class EmailNotification : public Notification {
    string sender_, recipient_, message_;
    int retries_;
    unique_ptr<string> signature_; // owned resource: requires deep copy
public:
    EmailNotification(const string& sender, int retries, const string& signature)
        : sender_(sender), retries_(retries), signature_(new string(signature)) {}

    EmailNotification(const EmailNotification& other)
        : sender_(other.sender_), recipient_(other.recipient_),
          message_(other.message_), retries_(other.retries_),
          signature_(new string(*other.signature_)) {}

    unique_ptr<Notification> clone() const override {
        return unique_ptr<Notification>(new EmailNotification(*this));
    }
    void setRecipient(const string& recipient) override { recipient_ = recipient; }
    void setMessage(const string& message) override { message_ = message; }
    void send() const override {
        cout << "From: " << sender_ << " | To: " << recipient_
             << " | Message: " << message_ << " | Retries: " << retries_
             << " | Signature: " << *signature_ << '\n';
    }
};

class NotificationRegistry {
    map<string, unique_ptr<Notification> > prototypes_;
public:
    void registerPrototype(const string& key, unique_ptr<Notification> prototype) {
        prototypes_[key] = std::move(prototype);
    }
    unique_ptr<Notification> create(const string& key) const {
        auto it = prototypes_.find(key);
        if (it == prototypes_.end()) throw invalid_argument("Unknown prototype: " + key);
        return it->second->clone();
    }
};

int main() {
    NotificationRegistry registry;
    registry.registerPrototype("welcome", unique_ptr<Notification>(
        new EmailNotification("noreply@example.com", 3, "Support Team")));

    auto alice = registry.create("welcome");
    alice->setRecipient("alice@example.com");
    alice->setMessage("Welcome, Alice!");

    auto bob = registry.create("welcome");
    bob->setRecipient("bob@example.com");
    bob->setMessage("Welcome, Bob!");

    alice->send();
    bob->send();
}
