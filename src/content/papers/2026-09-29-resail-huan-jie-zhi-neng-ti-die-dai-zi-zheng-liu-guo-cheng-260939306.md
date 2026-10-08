---
title: 'ReSAIL: Mitigating Collapse in Iterative Agent Self-Distillation'
title_zh: ReSAIL：缓解智能体迭代自蒸馏过程中的性能坍缩
authors:
- Shengjie Jin
- Hengbo Xu
- Zelong Sun
- YuJie Guo
- Zhiwu Lu
affiliations:
- Gaoling School of Artificial Intelligence, Renmin University of China
arxiv_id: '2609.39306'
url: https://arxiv.org/abs/2609.39306
pdf_url: https://arxiv.org/pdf/2609.39306
published: '2026-09-29'
collected: '2026-10-08'
category: Agent
direction: Agent 迭代自优化性能坍缩缓解
tags:
- LLM Agent
- Self-Distillation
- Performance Collapse
- Recursive Self-Improvement
- Privileged Information
one_liner: 提出插件式迭代自蒸馏增强方案ReSAIL，有效缓解LLM智能体迭代自优化的性能坍缩
practical_value: '- 做Agent迭代自优化时可复用Sensitivity-Guided Selection（SGS）筛选高价值交互步骤，仅用Top
  5%~25%的步骤就能获得比全量数据更好的效果，降低训练成本

  - 迭代知识蒸馏场景下可加入Privileged Retention（PR）正则项，保留模型的特权信息条件行为，避免多轮蒸馏后作为教师的能力退化

  - 离线轨迹数据筛选时可复用PI敏感性指标（普通视图与特权视图输出的JSD），优先保留对特权信息敏感的样本，提升蒸馏效率

  - 多轮自蒸馏的损失计算可采用Trajectory Loss Balancing，按轨迹平均损失避免长轨迹权重过高，平衡不同轨迹的贡献'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
迭代自蒸馏是LLM Agent实现递归自提升（RSI）的核心路径，但现有方法（如SDPO、OEL）在多轮迭代后会出现部署性能和特权信息（PI）条件性能的双坍缩，无法持续获得性能提升，阻碍了Agent自优化的落地。

### 方法关键点
1. **Trajectory-Balanced Selective Distillation（TBSD）模块**：用PI敏感性（同一步骤下模型普通视图与特权视图输出的JSD）筛选Top ρ的高价值交互步骤，再按轨迹平均损失平衡不同长度轨迹的权重，避免长轨迹占比过高
2. **Privileged Retention（PR）模块**：新增正则项约束学生模型的特权视图输出与冻结教师一致，保留模型作为下一轮蒸馏教师的PI条件能力，避免多轮迭代后教师能力退化
3. 整体为插件式增强方案，可直接集成到现有PI-based自蒸馏框架中，无需额外环境交互

### 关键实验
在ALFWorld、TextCraft两个文本Agent基准，以及多模态GUI Agent基准AITZ上测试，对比ReAct、SDPO、OEL等基线：集成到SDPO、OEL后，3轮迭代后最终成功率平均提升22.5个百分点，全程无性能下降；AITZ上仅用SGS筛选Top 80%的步骤，动作预测准确率提升1.06个百分点；训练成本仅为基线的1.23倍，选择Top 5%步骤时训练成本反而降低6%。

最值得记住的一句话：迭代自蒸馏需要同时兼顾当前部署模型的性能提升，以及模型作为下一轮教师的特权信息条件能力保留，二者缺一不可。
