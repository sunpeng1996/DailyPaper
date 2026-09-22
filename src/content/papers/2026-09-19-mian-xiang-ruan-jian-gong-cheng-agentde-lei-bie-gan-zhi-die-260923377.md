---
title: 'One to More, More to One: Category-Aware Iterative Expert Training for Software
  Engineering Agents'
title_zh: 面向软件工程Agent的类别感知迭代专家训练方法
authors:
- Jie Zhao
- Ziyu Jiang
- Suhang Zheng
- Minghui Shan
- Xiaoxiao Xu
- Lin Qu
affiliations:
- Alibaba Group
arxiv_id: '2609.23377'
url: https://arxiv.org/abs/2609.23377
pdf_url: https://arxiv.org/pdf/2609.23377
published: '2026-09-19'
collected: '2026-09-22'
category: Agent
direction: Agent 分域专家训练与能力融合
tags:
- AgentTraining
- MultiTeacherDistillation
- ReinforcementLearning
- TaskCategorization
- LLMAlignment
one_liner: 提出类别感知分域专家迭代训练+多教师蒸馏框架，解决多任务类别训练的性能跷跷板问题
practical_value: '- 多场景电商/推荐训练可直接复用「分场景训专家+多教师蒸馏合并」思路，解决跨场景性能跷跷板问题，无需依赖外部标注数据

  - RRE（Refresh-Repair-Expand）迭代训练trick可复用到多目标RL训练：每次RL后刷新任务掌握度，复用自身成功轨迹做Repair SFT，再扩展任务池，兼顾能力巩固与泛化

  - 标签路由+ReLU门控奖励外推的蒸馏方案可用于多场景模型压缩，仅保留各场景专家的正向提升方向，避免能力抵消

  - 证据驱动的多轴任务标注思路可用于电商用户/物品/推荐任务分层，提升训练数据的利用效率'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有同域多类别任务混合RL训练存在「类别跷跷板」问题：部分任务类别性能提升的同时其他类别出现退化，聚合指标完全掩盖了内部性能分布的不均衡；同时固定训练池会随着模型能力提升逐渐失去训练信号，缺乏针对同域下细分任务类别的专项训练与无损能力融合方案。

### 方法关键点
- 设计SWE Labeler多轴标注系统，从任务类型、所属领域、修改规模、认知复杂度等维度对任务做证据驱动的标准化标注，划分3个可路由的训练类别
- 每个类别独立执行RRE迭代训练循环：交替用Agentic-miniRL做长 horizon 强化学习，刷新模型对实例的掌握度，复用自身验证通过的成功轨迹做Repair SFT，再扩展任务池进入下一轮迭代，全程无需外部教师提供解决方案
- 采用标签路由的多教师On-Policy蒸馏（MOPD）合并多个类别专家的能力，加入ReLU门控奖励外推，仅保留每个教师相对基线的正向提升方向，避免不同类别能力互相抵消

### 关键结果
在Pro-618、SWE-bench Multilingual数据集上测试，对比Pooled RL、Balanced RL等基线，最终MOPD策略在Pro-618上平均准确率达58.04%，比基线提升5.39个百分点；在SWE-bench Multilingual上准确率达59.00%，比基线提升2.78个百分点，同时所有类别均实现正向提升，大幅缩小了性能跷跷板的差距。

**最值得记住的结论**：同域下细分任务类别的专项训练+定向能力融合，能同时提升聚合性能和细分场景的能力下限，避免多任务训练的能力抵消。
