// **********************************************
//                   TRY
// **********************************************

//Today we are continuing the stack data structure but with classes/constructors
//this time instead of arrays. 
//Remember, stack structures are first in, last out like a stack of Pringles (:
//You could also say last in, first out
//There is a display method already given to you below, so you can test the stack  

//This creates the nodes that will be placed in the stack
class ListNode {
    constructor(value) {
        this.value = value;
        this.next = null;
    }
}

// This is creating the stack itself.  
// Head is where things get added (beginning) to the stack so it's the top
// Tail is the last thing that needs to be removed so it's at the bottom
// The order of the stack will go from right (1st Node) to left (last node)   
// For example:   3rd Node (head) - 2nd Node - 1st Node (tail)
class SLLStack {
    constructor() {
        this.head = null;
        this.tail = null;
    }

    // Use add(value) to add something ot the top (head) of the stack 
    // Return the added node's value
    // HINTS - Need to create the node before you can add it
    // Remember to connect the node to the top of the stack first and then name it the new head
    // Edge Case - what if the list is empty?
    add(value) {
        var new_node = new ListNode(value);
        
        if (this.head == null) {
            this.head = new_node;
            this.tail = new_node;
        }
        else {
            new_node.next = this.head;
            this.head = new_node;
        }
    }
    //         if(this.head == null){
    //             // this.head.next = value
    //             this.head = new_node;
    //             this.tail = new_node;
    //         }
    //         else{
    //             this.head = 
    //         }
    // }
    

    // Use remove() to take away the node on top of the stack 
    // Return the removed node's value
    // HINTS - The head is the top of the stack
    // We need to save the head in a var before we remove it so we can return it's value
    // Name the new head and then cut the connection to the old head
    // Edge Cases - what if the list is empty?  What if there's only one node in the list?
    remove() {
        if (this.head == null) {
            return "Empty"
        }

        else {
            var output = this.head
            var temp = this.head.next
            this.head.next = null
            this.head = temp
        }
        return output
    }


    // Use top() to return the value of the top node of the stack without removing it
    // Edge Case - What if the list is empty?
    top() {
        
    }

    // Use contains(value) to search the stack for a received value
    // Return true if the value is in the stack, return false if it's not
    // There are no built in "stack" methods like "includes" in JS 
    // So how do we go through a whole stack?  Wanna go for a run....? (:
    contains(value) {
        
    }

    // Use isEmpty() to see if the stack is empty
    // Return true if the stack is empty, return false if it's not
    isEmpty() {
        
    }

    // Use size() to count all the nodes in the stack
    // Return the total number of nodes the stack
    // Edge Case - What if the list is empty?
    size() {
        
    }
    // This is given to you for your convenience, nothing to do here (:
    display() {
        if (this.head == null) {
            return null;
        }
        var values = this.head.value;
        var runner = this.head.next;

        while (runner != null) {
            values += " - " + runner.value;
            runner = runner.next;
        }
        return values;
    }
}

var x = new SLLStack();

console.log(x.isEmpty());
console.log(x.add("A"));
console.log(x.display());
console.log(x.isEmpty());

console.log(x.add("B"));
console.log(x.add("C"));
console.log(x.display());
console.log(x.top());

console.log(x.remove());
console.log(x.remove());
console.log(x.display());

console.log(x.add("D"));
console.log(x.add("E"));
console.log(x.display());
console.log(x.top());
console.log(x.size());
console.log(x.contains("E"));
console.log(x.contains("Z"));


// **********************************************
//                   ANSWER
// **********************************************

//Today we are continuing the stack data structure but with classes/constructors
//this time instead of arrays. 
//Remember, stack structures are first in, last out like a stack of Pringles (:
//You could also say last in, first out
//There is a display method already given to you below, so you can test the stack  

//This creates the nodes that will be placed in the stack
class ListNode {
    constructor(value) {
        this.value = value;
        this.next = null;
    }
}

// This is creating the stack itself.  
// Head is where things get added (beginning) to the stack so it's the top
// Tail is the last thing that needs to be removed so it's at the bottom
// The order of the stack will go from right (1st Node) to left (last node)   
// For example:   3rd Node (head) - 2nd Node - 1st Node (tail)
class SLLStack {
    constructor() {
        this.head = null;
        this.tail = null;
    }

    // Use add(value) to add something ot the top (head) of the stack 
    // Return the added node's value
    // HINTS - Need to create the node before you can add it
    // Remember to connect the node to the top of the stack first and then name it the new head
    // Edge Case - what if the list is empty?
    add(value) {        
        var node = new ListNode(value);
        
        if (this.head == null) {
            this.head = node;
            this.tail = node;
        }
        else {
            node.next = this.head;
            this.head = node;
        }
        return node.value
    }
    

    // Use remove() to take away the node on top of the stack 
    // Return the removed node's value
    // HINTS - The head is the top of the stack
    // We need to save the head in a var before we remove it so we can return it's value
    // Name the new head and then cut the connection to the old head
    // Edge Cases - what if the list is empty?  What if there's only one node in the list?
    remove() {
        if (this.head == null){
            return undefined;
        }
        else if (this.head == this.tail) {
            var temp = this.head;
            this.head = null;
            this.tail = null;
            return temp.value;
        }

        var temp = this.head
        this.head = this.head.next
        temp.next = null

        return temp.value
    }

    // Use top() to return the value of the top node of the stack without removing it
    // Edge Case - What if the list is empty?
    top() {
        if (this.head == null) {
            return undefined;
        }
        return this.head.value
    }

    // Use contains(value) to search the stack for a received value
    // Return true if the value is in the stack, return false if it's not
    // There are no built in "stack" methods like "includes" in JS 
    // So how do we go through a whole stack?  Wanna go for a run....? (:
    contains(value) {
        var runner = this.head;

        while (runner != null) {
            if (runner.value == value) {
                return true;
            }
            runner = runner.next;
        }
        return false;
    }

    // Use isEmpty() to see if the stack is empty
    // Return true if the stack is empty, return false if it's not
    isEmpty() {
        if (this.head == null){
            return true
        }
        else {
            return false
        }
    }

    // Use size() to count all the nodes in the stack
    // Return the total number of nodes the stack
    // Edge Case - What if the list is empty?
    size() {
        var count = 0

        if (this.head == null) {
            return count
        }
        else {
            var runner = this.head
            while (runner != null){
                count++
                runner = runner.next
            }
            return count
        }
    }
    // This is given to you for your convenience, nothing to do here (:
    display() {
        if (this.head == null) {
            return null;
        }
        var values = this.head.value;
        var runner = this.head.next;

        while (runner != null) {
            values += " - " + runner.value;
            runner = runner.next;
        }
        return values;
    }
}

var x = new SLLStack();

console.log(x.isEmpty());
console.log(x.add("A"));
console.log(x.display());
console.log(x.isEmpty());

console.log(x.add("B"));
console.log(x.add("C"));
console.log(x.display());
console.log(x.top());

console.log(x.remove());
console.log(x.remove());
console.log(x.display());

console.log(x.add("D"));
console.log(x.add("E"));
console.log(x.display());
console.log(x.top());
console.log(x.size());
console.log(x.contains("E"));
console.log(x.contains("Z"));