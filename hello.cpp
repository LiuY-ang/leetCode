//  Definition for singly-linked list.
#include <stdio.h>
#include <sys/malloc.h>
struct ListNode {
      int val;
      struct ListNode *next;
 };

struct ListNode* mergeTwoLists(struct ListNode* l1, struct ListNode* l2) {
    ListNode* head = (ListNode*)malloc(sizeof(ListNode));
    head->next=NULL;
    ListNode* tail = head;
    while( l1!=NULL && l2!=NULL )
    {
      if ( l1->val < l2->val )
      {
          tail->next=l1;
          l1=l1->next;
      }
      else  //l1->val >= l2->val
      {
        tail->next=l2;
        l2=l2->next;
      }
      tail=tail->next;
    }
    if (l1!=NULL)
      tail->next=l1;
    if(l2!=NULL)
      tail->next=l2;
    return head->next;
}

int main() {
  /* code */
  ListNode* l1=(ListNode*)malloc(sizeof(ListNode));
  l1->val=1;
  l1->next=NULL;
  ListNode* l2=(ListNode*)malloc(sizeof(ListNode));
  l2->val=2;
  l2->next=NULL;
  ListNode* head=mergeTwoLists(l1,l2);
  while(head!=NULL)
  {
    if(head->next == NULL)
      printf("%d\n",head->val );
    else
      printf("%d ",head->val);
    head=head->next;
  }
  return 0;
}
