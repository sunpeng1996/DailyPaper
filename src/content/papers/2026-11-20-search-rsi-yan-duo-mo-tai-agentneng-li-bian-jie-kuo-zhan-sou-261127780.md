---
title: 'Search-RSI: Expanding Search Worlds Along Multimodal Agents'' Capability Frontier'
title_zh: Search-RSI：沿多模态Agent能力边界扩展搜索世界
authors:
- Chengchao Lv
- Yin Wang
- Chunzheng Zhu
- Wanli Chang
affiliations:
- Hunan University
- New York University
arxiv_id: '2611.27780'
url: https://arxiv.org/abs/2611.27780
pdf_url: https://arxiv.org/pdf/2611.27780
published: '2026-11-20'
collected: '2026-11-23'
category: Agent
direction: 多模态搜索Agent 递归自改进训练
tags:
- Multimodal Agent
- Recursive Self-Improvement
- Reinforcement Learning
- Retrieval System
- Search Agent
one_liner: 提出递归自改进框架同步扩展任务与检索库，解决多模态搜索Agent训练不可达负样本问题
practical_value: '- 训练电商导购、商品搜索类Agent时，可复用任务与检索库同步扩增策略，避免正确搜索行为因证据缺失被误惩罚，减少训练噪声

  - 能力边界诊断方法可直接迁移到Agent课程学习：按跳数、关系稀有度、干扰密度划分任务单元，优先选择成功率0.2~0.8的部分掌握单元生成训练任务，提升训练效率

  - 无外部教师的自演示trick可复用：对完全超出当前能力的任务，给出路径特权提示生成正确轨迹，移除提示后作为监督样本，无需额外标注即可覆盖难例

  - 工程上可复用staged commit机制：新任务的证据先写入隔离索引验证，仅保留有效任务的证据合并到正式检索库，避免检索库无效膨胀引入干扰'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有多模态搜索Agent的在线任务生长范式默认检索库固定，实测29%的新生成任务缺少对应支撑证据，导致Agent执行正确搜索却被误惩罚，这类不可达负样本占所有负奖励的41%，严重干扰训练信号；同时任务分配无针对性，完全超出能力边界的任务RL无法获得有效梯度，训练容易提前饱和。
### 方法关键点
- 边界诊断：按跳数、关系稀有度、干扰密度划分3×3×3任务单元，计算每个单元的成功率方差与跳命中率方差，优先给成功率在0.2~0.8区间的部分掌握单元分配任务配额
- 同步支撑注入：按边界单元采样生成新任务，将任务依赖的证据先写入隔离staged索引，仅保留有效任务的证据合并到正式检索库，避免无效证据膨胀
- 策略引导准入：用当前策略做探针，部分答对的任务进入RL训练，全错的任务给路径提示重试生成正确轨迹，作为自演示监督样本，无需外部教师
- 递归闭环：每轮训练后的新策略作为下一轮的诊断、探针、演示生成器，实现能力与任务边界同步扩展
### 关键结果
在9个多模态搜索基准上测试，相比静态生长基线，9B模型平均准确率提升10.4个点，27B模型提升10.2个点，仅增加27%计算量；不可达负样本占比从41%降至4.4%，环境一致性从0.85升至0.98。
> 最值得记住的结论：搜索Agent训练中检索库不应是固定背景，而是要和任务、Agent能力同步生长的训练变量
