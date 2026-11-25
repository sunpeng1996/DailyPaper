---
title: 'Lazy Agents Answer Against Their Own Beliefs: Reinforcement Learning with
  Verifiable Beliefs Teaches Them to Act on What They Believe'
title_zh: 基于可验证信念的强化学习 纠正Agent违背自身信念的懒惰行为
authors:
- Richmond Sin Jing Xuan
- Peilin Feng
- Wenbin Wang
- Soujanya Poria
affiliations:
- Nanyang Technological University, Singapore
arxiv_id: '2611.32884'
url: https://arxiv.org/abs/2611.32884
pdf_url: https://arxiv.org/pdf/2611.32884
published: '2026-11-23'
collected: '2026-11-25'
category: Agent
direction: Agent 决策优化 · 强化学习训练
tags:
- Reinforcement Learning
- Agent Training
- Process Reward
- Metacognition
- POMDP
one_liner: 提出RLVB强化学习框架 利用可验证后验信念训练Agent避免过早提交答案
practical_value: '- 电商导购、搜索意图探索类多轮交互Agent可复用RLVB逻辑，训练Agent基于已收集的用户交互/查询证据判断终止时机，避免证据不足时提前给出不符合需求的推荐/搜索结果

  - 有沙箱模拟环境的Agent训练场景，可直接用环境计算的精确后验作为过程奖励，无需额外训练Reward Model或调用LLM Judge，相比GRPO/PPO效果更好且GPU成本降低37.5%

  - 可在Agent交互流程中强制增加每轮信念输出模块（如当前已确定的需求、待确认选项），无需为信念设置额外奖励，仅通过梯度关联信念与动作即可大幅降低提前终止比例'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
长任务Agent普遍存在「懒惰行为」：在证据不足、自身信念仍存在多个可能答案时就提前提交结果，最终准确率低。传统仅基于最终结果的RL奖励无法区分蒙对的幸运猜测和有充分证据的正确答案，无法教会Agent正确判断终止时机；基于LLM Judge的过程奖励训练成本高，还会错误奖励符合真实结果但证据不足的猜测。
### 方法关键点
- 提出RLVB框架，利用训练时沙箱模拟器的特权信息计算每一步答案的精确后验作为可验证信念，无需额外Reward Model、Critic或LLM Judge
- 基于精确后验定义教师策略输出过程奖励：证据不足时奖励继续收集信息，证据充分时奖励提交答案，惩罚提前提交行为；奖励不读取Agent输出的信念文本，仅通过梯度更新自动关联信念输出和动作决策
- 支持组相对策略梯度、EM两种优化器，仅对比同历史下的多轮采样动作计算权重，解决传统轨迹RL的信用分配错误问题
### 关键结果
在3个开源VL模型、3个基准数据集（训练任务域内的HiddenGames、零样本迁移的Pro-Worlds/RoboQuest）的9组测试设定中，RLVB均超越Base模型，平均准确率提升17.1%，比基于LLM Judge的PPO平均高9.3%，GPU小时数仅为后者的1/1.6；提前提交答案的比例从Base的76%~87%降至44%~46%，证据充分时才提交的比例最高提升43pct。
> 最值得记住的结论：Agent准确率提升核心来自于在更高证据水平下提交答案，而非单步证据收集效率或信念识别准确率的提升，仅将动作决策与自身信念绑定即可获得显著收益
