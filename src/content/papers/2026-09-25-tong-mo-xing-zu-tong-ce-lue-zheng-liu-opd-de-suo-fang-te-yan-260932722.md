---
title: Scaling Properties of Same-Family On-Policy Distillation
title_zh: 同模型族同策略蒸馏（OPD）的缩放特性研究
authors:
- Yuntai Bao
- Qinfeng Li
- Guoqing Jiang
- Liwei Chen
- Zhiheng Qin
- Xuanping Li
- Wenqi Zhang
- Xuhong Zhang
affiliations:
- Zhejiang University
- Kuaishou Technology
arxiv_id: '2609.32722'
url: https://arxiv.org/abs/2609.32722
pdf_url: https://arxiv.org/pdf/2609.32722
published: '2026-09-25'
collected: '2026-10-01'
category: Training
direction: LLM训练 · 同策略蒸馏缩放规律
tags:
- On-Policy Distillation
- Scaling Law
- Knowledge Distillation
- Weak-to-Strong Generalization
- RLHF
one_liner: 揭示同策略蒸馏的缩放规律，可基于师生规模与得分提前预测蒸馏效果
practical_value: '- 业务域LLM蒸馏优先选择相同精度下参数量更小的teacher，不仅蒸馏效果更好，还能降低teacher侧的推理成本

  - 弱到强蒸馏场景直接使用纯OPD即可，不要加off-policy SFT冷启动，师生能力差越大冷启动精度损失越高，14B学生配0.5B teacher的场景下冷启动会损失32个精度点

  - 弱到强蒸馏无需做多步bootstrap，直接用最小规模的RL expert一步蒸馏即可，多步bootstrap反而会导致最终效果下降1个百分点以上

  - 可复用论文提出的联合幂律公式提前预估OPD后的模型峰值精度，无需跑完全部训练流程，外推最大规模模型的误差小于0.7个精度点，大幅节省训练试错成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前LLM后训练pipeline中On-Policy Distillation（OPD）被广泛用于跨模型迁移RL训练获得的推理能力，但OPD效果与师生模型规模的对应关系缺乏系统性研究，无法提前预测蒸馏结果，只能完成全量训练后才能评估效果，造成大量计算资源浪费。
### 方法关键点
- 覆盖三种OPD师生设置：强到弱、同基座、弱到强，定义 $d=\sqrt{KL(学生策略与初始化的token级反向KL)}$ 作为训练进度统一指标
- 对比两种主流OPD目标：Vanilla-OPD、Delta-OPD，同时验证off-policy冷启动、多步bootstrap等常见工程方案的实际效果
- 基于Qwen2.5 0.5B~14B全系列模型在数学推理任务上做受控实验，拟合OPD峰值精度、有效迁移阶段斜率的联合幂律预测公式
### 关键结果
- OPD训练分为两阶段：初始有效迁移阶段gold score随d线性提升，线性拟合$R^2$达0.932~0.988；后续阶段动态异构，无统一规律
- 弱到强蒸馏场景下学生峰值精度必然超过teacher，联合幂律外推最大规模模型的预测误差<0.7个点（Vanilla-OPD）、<0.4个点（Delta-OPD）
- 相同精度下更小的teacher迁移效果更好，off-policy冷启动在大能力差场景精度损失高达19.4个点，多步bootstrap比直接一步蒸馏效果低1个点以上

RL推理能力只需在小模型上训练一次，就可通过OPD可预测地迁移到同家族更大模型上，大幅降低大模型RL训练成本
