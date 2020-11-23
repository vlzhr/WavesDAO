# Smart Contract for Waves DAO

VIDEO DEMO ---> https://www.youtube.com/watch?v=fGzLHMJmR0o

You can try it in the auto UI: https://waves-dapp.com/3MsJ87eiwhT5eUMCmwjVm7VqP74qs48RheF

## DAO Mission

DAO (decentralized autonomous organization) is a tool for decentralized and trasparent governance. 

This DAO model is proposed to use inside of Waves Association team to make decisions about granting projects and researches. Read about process details below.

## Principles

This DAO is based on some principles identified during DAO research by Vladimir Zhuravlev: https://medium.com/wavesprotocol/dao-2020-whats-missing-b717c4c64232

These are:

- tokenless
- simple UI
- simple roles and behaviour models

## DAO roles

DAO Owner - the administrator for a DAO. Could be a group of people (MultiSig) in the following versions.

DAO Member - a whitelisted person that can take part in the votings. For the decisions DAO needs 50%+ to vote.

Working Group Member - a whitelisted person who is responsible to manage tasks, votings and performers.

## Happy Path

This is the simplest algorithm to make decisions in the Waves Association DAO for three user roles: DAO Owner (DO), DAO Member (DM), Working Group Member (WG).

In addition, there are Performers (PE) who apply and complete bounties.

### Setting DAO

1. **DO:** sets the DM list *(addDAOMember)*
2. **DO:** sets the WG list *(addGroupMember)*

### Making Funds Decisions

**Disruptive Tech Grant**

1. **WG:** proposes task *(addTask)*
2. **WG:** adds task description and reward amount *(addTaskDetails)*
3. **DM:** votes on task (do we really need it?) *(voteForTaskProposal)*
4. **WG:** finishes voting on the task *(finishTaskProposalVoting)*
5. **PE:** applies for performing the task *(applyForTask)*
6. **DM:** votes on task applicants (choose the performer) *(voteForApplicant)*
7. **WG:** finish performer election *(finishApplicantsVoting)*
8. **PE:** starts work on the bounty *(startWork)*
9. **PE** & **WG**: off-chain communication
10. **WG:** accepts a solution and pays a reward *(acceptWorkResult)*

**Web3.0 Development Grant**

1. **PE:** proposes solution *(addTask)*
2. **PE:** adds solution description and requested reward amount *(addTaskDetails)*
3. **WG:** initializes a voting on solution *(initTaskVoting)*
4. **DM:** votes on task (do we really need it?) *(voteForTaskProposal)*
5. **WG:** finishes voting on the task *(finishTaskProposalVoting)*
6. **PE:** starts work on the bounty *(startWork)*
7. **PE** & **WG**: off-chain communication
8. **WG:** accepts a solution and pays a reward *(acceptWorkResult)*

**Interhack Grant**

1. **WG:** proposes task *(addTask)*
2. **WG:** adds task description and reward amount *(addTaskDetails)*
3. **DM:** votes on task (do we really need it?) *(voteForTaskProposal)*
4. **WG:** finishes voting on the task *(finishTaskProposalVoting)*
5. **PE:** applies for performing the task *(applyForTask)*
6. **DM:** votes on task applicants (choose the hackathon participants) *(voteForApplicant)*
7. **WG:** finish participants election *(finishApplicantsVoting)*
8. **WG:** sets jury list & starts hackathon *(enableSubmissions)*
9. **PE:** submit solutions *(submitSolution)*
10. **WG:** stops accepting submissions *(stopSubmissions)*
11. **JURY:** votes on solutions *(voteForSolution)*
12. **WG:** accepts the best solution and pays a reward *(acceptWorkResult)*

## Play Around

https://waves-dapp.com/3MsJ87eiwhT5eUMCmwjVm7VqP74qs48RheF

## Read source code

https://waves-ide.com/s/5f33b6fcd4504a002b45a58d
