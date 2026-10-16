---
title: Training-Free On-Policy Distillation
title_zh: 无需训练的同策略蒸馏 高效聚合多领域大模型专家能力
authors:
- Bangji Yang
- Jiajun Fan
- Zhaoyu Zhu
- Hongbo Ma
- Ge Liu
affiliations:
- University of Illinois at Urbana-Champaign
- Tsinghua University
arxiv_id: '2610.22236'
url: https://arxiv.org/abs/2610.22236
pdf_url: https://arxiv.org/pdf/2610.22236
published: '2026-10-15'
collected: '2026-10-16'
category: Training
direction: 大语言模型 · 免训练同策略蒸馏
tags:
- Knowledge Distillation
- On-Policy Distillation
- Model Merging
- Training-Free
- LLM Fine-tuning
one_liner: 仅通过前向传播与线性运算实现无训练多领域LLM专家融合 平均精度超单领域专家
practical_value: '- 业务侧多场景LLM专家（如搜索query理解、商品文案生成、客服应答）可直接用TF-OPD融合，无需额外训练，成本远低于多任务微调/传统蒸馏，上线速度快

  - 融合样本过滤trick可复用：删除重复循环、无效的生成样本，仅保留高质量on-policy样本统计量，能大幅提升融合模型在难例上的表现，避免无效token主导权重

  - 数值精度选择经验可迁移：RL微调后的模型权重变动极小，融合后的模型用float16存储/推理即可避免精度损失，平衡效果与显存占用'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有同策略蒸馏需大量rollout、教师前向与梯度迭代，成本极高；传统权重算术融合不考虑专家的on-policy输入分布，融合RL微调的多领域专家时会丢失原领域能力，难以兼顾多场景效果。
### 方法关键点
- 假设所有专家共享同一基座模型，将单层蒸馏目标转化为最小二乘问题，仅需各专家输入的二阶矩即可得到闭式解，全程无梯度计算
- 收集各专家在自身领域生成的rollout，过滤重复循环、未正确结束的无效样本后，通过前向传播记录每层输入的Gram矩阵，取α=0.9收缩二阶矩非对角元保证求解稳定
- 按层求解得到融合权重，embedding、归一化层等非线性映射层用任务算术融合，仅需前向计算与线性代数运算
### 关键结果
基于Olmo 3 7B的数学、代码单领域专家实验，对比基座、单专家、任务算术等基线：在7个数学+代码基准上，TF-OPD平均精度达61.1%，超过数学专家的59.8%与代码专家的53.6%，单领域精度损失不到2%；仅需约10 GPU小时即可完成融合，删除无效循环样本后AIME25精度从34.2%提升至40%，对齐同精度下的数学专家水平。
最值得记住的一句话：共享基座的多领域专家聚合无需训练，on-policy样本的质量比融合算法复杂度更决定难例表现。
