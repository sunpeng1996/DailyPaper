---
title: 'Reflection Is Not Always Worth It: Budgeted Reflection Allocation for Recommendation
  Agents'
title_zh: 反思并非总能带来增益：面向推荐Agent的预算化反思分配框架
authors:
- Jinfeng Xu
- Zheyu Chen
- Ziyue Peng
- Jianheng Tang
- Zheng Lin
- Wenhao Yuan
- Jian Chen
- Shujie Li
- Victor Leung
affiliations:
- The University of British Columbia
- The Hong Kong Polytechnic University
- The Hong Kong University of Science and Technology
- Peking University
- University of Luxembourg
arxiv_id: '2611.19847'
url: https://arxiv.org/abs/2611.19847
pdf_url: https://arxiv.org/pdf/2611.19847
published: '2026-11-15'
collected: '2026-11-17'
category: Agent
direction: 推荐Agent · LLM反思资源分配
tags:
- Recommendation Agent
- Reflection Allocation
- LLM4Rec
- Budgeted Learning
- Uncertainty Estimation
one_liner: 基于排序脆弱性门控信号实现推荐Agent训练阶段LLM反思的预算化分配，兼顾成本与推荐效果
practical_value: '- 训练阶段LLM反思无需全量覆盖用户，优先给top-K排序分数差小（排序脆弱）的用户分配LLM资源，60%预算即可达到甚至超过全量反思的效果，大幅降低LLM调用成本

  - 跨工具/模型的结果不一致不能直接作为分配LLM资源的信号，必须先经过排序脆弱性门控，否则反而会引入噪声拉低效果

  - 该框架无需修改原有推荐工具链、LLM Prompt、推理链路，仅需在训练阶段新增预计算的分配逻辑即可落地，侵入性极低'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前LLM驱动的推荐Agent普遍对所有训练用户执行全量LLM反思，调用成本高且收益不均：部分用户的排序结果已稳定，LLM反思无法带来增益甚至会引入噪声扰动可靠的工具混合权重，因此需要在有限LLM预算下，精准选择能从反思中获得最大收益的用户。
### 方法关键点
- 提出BRAVE预算化反思分配框架，仅用推荐侧预计算的低成本信号实现分配，无需额外模型训练或LLM调用，不修改原有推理链路、推荐工具、Prompt设计
- 核心采用门控双信号机制：第一优先级信号为排序脆弱性（所有推荐工具的top1与top2平均分差的负值，分差越小脆弱性越高），仅当脆弱性超过阈值时，才引入第二信号跨工具不一致（各推荐工具top-K结果的Jaccard相似度的负值，重叠越低不一致越高）计算最终分配得分
- 训练阶段仅对得分最高的前B%用户执行LLM反思更新工具混合权重，其余用户仅用无LLM的排序比较信号更新权重
### 关键实验
在Amazon、Yelp、Goodreads三个全排序推荐基准数据集上测试，对比全量反思的PRTA基线：60%LLM预算下的BRAVE仅用66%的训练LLM调用量，最高可提升NDCG@20 0.53个百分点，效果优于随机分配、仅用不一致信号等消融方案，且适配GPT-4o、Qwen3-8B等各类闭源/开源LLM控制器。
### 核心结论
推荐Agent的优化方向不止是更强的反思模块，更应该关注什么时候该调用LLM反思，把昂贵的计算资源用在能产生实际增益的场景。
