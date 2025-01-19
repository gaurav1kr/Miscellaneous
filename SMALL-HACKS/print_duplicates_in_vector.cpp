void dupicate(vector<int> &V)
{
    unordered_set<int> store;
    
    for(auto it:V)
    {
        if(store.find(it)!=store.end())
        {
            cout<<it<<" ";
        }
        else
        {
            store.insert(it);
        }
    }
}
