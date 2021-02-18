# Waves DAO

*The Waves DAO is a dApp developed on the Waves blockchain and used as a decision making tool by the Waves Association, which sets up development directions for the entire ecosystem and makes strategic decisions on the  products. To get a basic understanding of what a DAO is, I suggest you check out this article: [What is a DAO?](https://medium.com/waves-association/what-is-a-dao-12fdb9abc681)*



This repository contains a source code of Waves DAO smart contracts. The frontend application is available at [Waves DAO App](https://github.com/rieset/waves-dao-app) repository. You can deploy smart contracts automatically with **deploy.py** script.



## User roles

The **DAO Manager** is a DAO administrator who has the right to set the working group and association member lists. Currently, the DAO Owner is a single account, to which the association’s secretary has access . The DAO Owner doesn’t participate in votes.



A **DAO Member** is any association member who was accepted by recommendation of the Membership Working Group, paid a membership fee and has the right to vote on grant distribution decisions. A list of accounts that have a DAO Member status is decided by the DAO Owner. Currently, it includes 30 association members.



A **Working Group Member** is a member of the Working Group for Funding & Grants. The working group’s task is to play an administrative role in the grant program management. Specifically, WG Members have to suggest grant assignments, open and close votes on grant issue and prepare reports on grant execution. Currently, the working group includes 8 people. Their accounts are added to the DAO by the secretary.



An **Applicant** is a user who is not added to the DAO member list. This is any community member who has applied for a grant using their Waves account. If their application has been approved and confirmed by voting of DAO Members, the user will be granted a **Performer** status.



The **Association Board** is an entity within the association, consisting of working group heads and the president. This entity doesn’t directly interact with the smart contract but, in real life, has the right to confirm a working group’s decisions. 



## Grant types

All user roles are involved in the grant distribution process, except for the DAO Owner. For convenience, we’ll use abbreviations: DAO Member (DM), Working Group Member (WG), Performer (PE), Association Board (BO).



### **Disruptive Tech Grants**

Grants of this type are suggested by association members. Normally, these are major development or research tasks that can be vital for the development and adoption of blockchain technology.

**Workflow:** 

(offchain) WG & RD & BO: discuss tasks

WG: proposes task

WG: adds a task description and reward amount

DM: votes on the task (do we really need it?)

WG: finishes voting on the task

PE: applies for performing the task

DM: votes on task applicants (choose the performer)

WG: finish performer election

PE: starts work on the bounty

PE & WG: off-chain communication

(offchain) WG & BO: agree on solution quality

WG: accepts a solution with a work report and pays a reward



A detailed diagram of participant interaction in the decision making process is available on the [Waves DAO website](https://dao.wavesassociation.org/assets/img/diagram_disruptive_2x.png).



### Web 3.0 Development Grants

Ideas for grants of this type are suggested by applicants. Normally, these are ideas for dApps or startups. You can check out Web 3.0 Grant ideas that have been approved so far in this [article](https://medium.com/waves-association/waves-association-distributes-first-web3-development-grants-59f72be35d3e).

**Workflow:**

PE: proposes a solution

PE: adds a solution description and requested reward amount

WG: initializes a vote on the solution

DM: votes on applications

WG: finishes voting on the task

PE: starts work on the bounty

(offchain) PE & WG: communication

(offchain) WG & BO: agree on paying a reward

WG: accepts the solution and pays a reward



A detailed diagram of participant interaction in the decision making process is available on the [Waves DAO website](https://dao.wavesassociation.org/assets/img/diagram_disruptive_2x.png).



### Interhack Grants

Grants of this type are as close as possible to the hackathon format, familiar to most developers. The association suggests an idea and offers a prize, and developers who pass preliminary selection compete in implementation of the idea.

**Workflow:**

(offchain) WG & RD & BO: discuss tasks

WG: proposes a task 

WG: adds a task description and reward amount

DM: votes on the task

WG: finishes voting on the task

PE: applies for participating in a hackathon

DM: votes on hackathon participants

WG: finish participant election

WG: sets up a jury list & starts the hackathon

PE: submit solutions

WG: stops accepting submissions

JURY: votes on solutions

WG: accepts the best solution and pays a reward



A detailed diagram of participant interaction in the decision making process is available on the [Waves DAO website](https://dao.wavesassociation.org/assets/img/diagram_disruptive_2x.png).



This type of grants implies another entity, the **JURY** - as list of addresses of DAO Members participating in the selection of winners. This is done to speed up the process of evaluating solutions after the completion of a hackathon, as it requires a smaller number of involved individuals.



## Looking forward

Grant distribution is the association’s main task. However, for harmonious and sustainable development, it has to implement other tasks, as well. The Waves DAO should become the main tool for running the association’s processes. Therefore, in the future, it should acquire functionality that is not directly related to the grant program.

For instance, the process of accepting new members should be moved to the DAO, from the working group voting stage to membership fee payment. This will help make the system independent and cyclical, ensuring an inflow of new DAO Members who will vote for project sponsorship.

The addition of other votes on changes in the Waves ecosystem is also possible. When the first grant batch was processed, the issue of insufficient verification of project tokens on Waves exchanges was discovered. One type of votes that could be added to the DAO is a vote by association members on token verification, with adding approved token’s avatars to Waves.Exchange.



## Message to developers

We welcome any enthusiasts to use DAO framework for their needs, contribute to this repository and leave feedback. Waves DAO is planned to be an open-source independent tool that can be helpful for any associations.
