//today we will be receiving a location and a value and will be adding that value
//before and after the given location yay!

class ListNode {
    constructor(value) {
        this.value = value;
        this.next = null;
    }
}

class SinglyLinkedList {
    constructor() {
        this.head = null;
        this.tail = null;
    }

    addToFront(value) {
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
    addToBack(value) {
        var new_node = new ListNode(value);
        if (this.head == null) {
            this.head = new_node;
            this.tail = new_node;
        }
        else {
            this.tail.next = new_node;
            this.tail = new_node;
        }
    }
    contains(target) {
        var runner = this.head;

        while (runner != null) {
            if (runner.value == target) {
                return true;
            }
            runner = runner.next;
        }
        return false;
    }
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
    removeFront() {
        if (this.head == null) {
            return null;
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
    removeBack() {
        if (this.head == null) {
            return null;
        }
        else if (this.head == this.tail) {
            var temp = this.head;
            this.head = null;
            this.tail = null;
            return temp.value;
        }
        let runner = this.head;
        while (runner != this.tail) {
            if (runner.next == this.tail) {
                let getEnd = this.tail;
                this.tail = runner;
                runner.next = null;
                return getEnd.value;
            }
            runner = runner.next;
        }
    }
    moveMinToFront() {
        var min = this.head
        var runner = this.head
        var walker = this.head

        while (runner.next != null) {
            if (runner.next.value < min.value) {
                min = runner.next
                walker = runner
            }
            runner = runner.next
        }

        if (min == this.head) {
            console.log("Minimum value is already at the front!")
            return
        }
        walker.next = min.next
        min.next = this.head
        this.head = min
    }
    moveMaxToBack() {
        var max = this.head
        var runner = this.head
        var walker = this.head

        while (runner.next != null) {
            if (runner.next.value > max.value) {
                max = runner.next
                walker = runner
            }
            runner = runner.next
        }

        if (max == runner) {
            console.log("the max is already at the back!")
            return
        }

        if (max == this.head) {
            this.head = this.head.next
        }
        walker.next = max.next
        max.next = null
        runner.next = max
    }

    //Use appendValue(loc,value) to receive a location in the list and a value
    //Add that value AFTER the location
    //EXAMPLE: appendValue(2,"Las Vegas") - will add a node with a value of "Las Vegas" AFTER the 2nd node, making it the 3rd
    //HINTS: You'll need a way to see when you've arrived at that location.  Some sort of counter maybe? (:
    //Once the runner has arrived, attach the node's next property to the runner's next
    //Then attach the runner's next property to the node you just placed into the list

    
    // appendValue(loc, value) {
    //     var runner = this.head
    //     var num =1
    //     while (runner.next != null){
    //         var runner = runner.next
    //         num+= 1
    //         if (num == loc){
    //             var temp = runner.next
    //             runner.next = ListNode(value)
    //             value.next = temp
    //         }
    //     } return 
    // }
    appendValue(loc,value){
        var node = new ListNode(value)
        var runner = this.head
        var counter = 1;
        while(counter < loc){  //this will get to the location given               
            runner = runner.next
            counter++
        }
        //this attaches the new node to the list by attaching it's next value to the runner's next value 
        node.next = runner.next   
        //now that the node's next value is attached to the runner's next value 
        //we can take those two values and place them into the list by setting the runner's next value to node
        runner.next = node   
    }

    //Use prependValue(loc,value) to receive a location in the list and a value
    //Add that value BEFORE the location
    //EXAMPLE: prependValue(2,"Las Vegas") - will add a node with a value of "Las Vegas" BEFORE the 2nd node, making it the 1st
    //HINTS: You'll need a way to see when you've arrived one node before the location
    //Once the runner has arrived one before, attach the node's next property to the runner's next
    //Then attach the runner's next property to the node you just placed into the list
    prependValue(loc, value) {
    }
    prependValue(loc,value){
        var node = new ListNode(value)

        if(loc == 1){
            node.next = this.head;
            this.head = node;
            return
        }

        var runner = this.head
        var counter = 1;
        while(counter < loc-1){ //this gets us one before the location given               
            runner = runner.next
            counter++
        }           
        node.next = runner.next  //this attaches the new node to the node at the given location
        runner.next = node //this tells the runner to be attached to the new node
    }
}


var new_sll = new SinglyLinkedList();
new_sll.addToBack("Disneyland");
new_sll.addToBack("Las Vegas");
new_sll.addToBack("Grand Canyon");
new_sll.addToBack("Times Square");
new_sll.addToBack("Mount Rushmore");
console.log(new_sll.display());

new_sll.appendValue(3, "Universal Studios")
console.log(new_sll.display());

new_sll.prependValue(3, "Smithsonian")
console.log(new_sll.display());
