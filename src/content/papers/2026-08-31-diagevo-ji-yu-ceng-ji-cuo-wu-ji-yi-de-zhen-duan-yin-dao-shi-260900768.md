---
title: 'DiagEvo: Diagnosis-Guided Self-Evolution via Hierarchical Error Memory'
title_zh: DiagEvo：基于层级错误记忆的诊断引导式大模型自进化框架
authors:
- Xincheng Wei
- Yifan Ding
- Yoshua Li
- Dongsheng Ma
- Rongxiang Weng
- Xunliang Cai
- Wenjian Ding
- Yao Zhang
affiliations:
- The Chinese University of Hong Kong, Shenzhen
- Meituan
- Peking University
- Juntendo University
- Nankai University
arxiv_id: '2609.00768'
url: https://arxiv.org/abs/2609.00768
pdf_url: https://arxiv.org/pdf/2609.00768
published: '2026-08-31'
collected: '2026-09-02'
category: Training
direction: LLM自进化 · 无监督自博弈训练
tags:
- Self-Play
- Hierarchical Memory
- Curriculum Learning
- Pseudo-Label Filtering
- LLM Reasoning
one_liner: 无需外部任务资源，通过层级错误记忆引导自博弈迭代，持续提升LLM推理性能
practical_value: '- 双置信度过滤可直接复用在生成式推荐/广告文案的伪标签提纯场景：对LLM生成的候选内容做多数投票，同时要求Top1得票率高于阈值且是Top2的τ倍以上，过滤低质量冲突样本，降低错误标注对下游模型的影响

  - 层级错误记忆可迁移到电商导购Agent、搜索Query理解模型的迭代流程：自动从失败case中提取通用错误原因，按技能维度归类并标记待优化/已掌握状态，定向生成训练样本补短板，大幅降低人工标注成本

  - 频率驱动的探索-利用平衡策略可用于推荐系统多目标迭代：给高频错误对应的优化方向分配更多流量，同时保留固定比例探索新场景，平衡短板补齐效率和业务创新覆盖度'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有无引导LLM自博弈方法易出现问题表面复杂度虚高、性能 plateau 甚至退化，而带引导的自进化方法依赖外部标注、文档库等额外资源，无法实现完全闭环的自主迭代，亟需一种能从模型自身运行数据中提取训练信号的自进化方案。
### 方法关键点
- 搭建层级错误记忆库：按技能节点归类通用错误原因，每个错误标记Active（待优化）/Mastered（已掌握）状态，跟踪错误在当前活跃周期的出现频率
- 诊断引导的样本生成：挑战者根据记忆状态混合生成样本，错误总频次越高，定向生成针对活跃错误样本的概率越高，同时保留固定比例自由探索；同技能下的已掌握错误可和活跃错误拼接生成综合样本，提升泛化性
- 双置信度伪标签过滤：除了要求多数投票率落在[plow, phigh]的中间难度区间的绝对约束，新增相对约束要求Top1答案得票率≥τ*Top2得票率，过滤高冲突不稳定样本
- 闭环记忆更新：诊断模块对比失败和成功轨迹的最早推理差异，提取通用错误原因更新记忆库，错误达标后自动标记为已掌握，复发时自动重新激活
### 关键结果
在Qwen3-4B/8B、OctoThinker-8B三个基座模型上测试9个推理benchmark，对比R-Zero、DARC等6个baseline：Qwen3-8B上数学推理平均准确率达72.3%，超R-Zero 4.5个百分点，超使用外部资源的DARC 1.2个百分点，整体准确率57.4%超DARC 1.1个百分点；仅用4B小模型做诊断即可达到最优效果，记忆相关额外开销仅占总runtime的5.7%。

模型自身的失败历史就是最精准的无监督训练课程信号，结构化的错误诊断能让自进化完全脱离外部资源也能持续稳定迭代。
