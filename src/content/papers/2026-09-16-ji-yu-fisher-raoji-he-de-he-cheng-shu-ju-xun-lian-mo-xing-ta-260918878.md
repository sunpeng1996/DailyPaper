---
title: 'Preventing Model Collapse: A Fisher-Rao Perspective on the Dynamics of Training
  with Synthetic Data'
title_zh: 基于Fisher-Rao几何的合成数据训练模型崩塌抑制理论研究
authors:
- Matteo Marchi
- João Pedro Silvestre
- Bahman Gharesifard
- Paulo Tabuada
affiliations:
- University of California, Los Angeles
- Queen's University
arxiv_id: '2609.18878'
url: https://arxiv.org/abs/2609.18878
pdf_url: https://arxiv.org/pdf/2609.18878
published: '2026-09-16'
collected: '2026-09-17'
category: Training
direction: 合成数据训练 模型崩塌抑制理论研究
tags:
- Model Collapse
- Synthetic Data
- Fisher-Rao Metric
- LLM Training
- Information Geometry
one_liner: 基于概率单纯形Fisher-Rao度量推导高维场景下抑制模型崩塌的最小真人数据比例下界
practical_value: '- 做生成式推荐/垂直领域Agent的迭代合成数据训练时，不能沿用欧氏度量给出的真人数据比例的乐观估计，高维item/语义场景下需至少调高1个数量级的真人标注数据占比，避免模型输出同质化崩塌

  - 高维推荐/搜索的用户/物品语义分布对齐任务，可借鉴Fisher-Rao度量替代传统欧氏/余弦距离，解决高维空间下分布差异被低估的问题，提升对齐精度

  - 迭代训练垂类LLM时，可参考文中推导的真人数据注入率阈值设置训练数据配比，减少多轮迭代后的效果退化，降低合成数据训练的试错成本'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前大模型训练面临高质量真人数据枯竭的瓶颈，复用合成数据迭代训练成为主流方案，但递归训练极易引发模型崩塌：模型输出逐渐同质化、偏离真实数据分布。过往基于欧氏度量推导的真人数据比例下界在高维场景下存在严重的度量失真问题，会给出过于乐观的低比例估计，无法实际指导训练。
### 方法关键点
- 采用适配概率单纯形的Fisher-Rao度量建模生成模型分布的迭代演化过程，避免高维下不同分布的欧氏距离趋近于0的度量失效问题
- 引入KL散度作为Lyapunov函数分析训练动力学的收敛性，推导训练过程中分布各维度取值的下界，保证Fisher-Rao度量在迭代过程中始终有效
- 结合训练温度系数、优化误差扰动边界等实际参数，严格推导抑制模型崩塌所需的真人/合成数据比例阈值，以及收敛后的分布误差上界
### 关键结果
高维场景下，若要实现Fisher-Rao误差随维度n增长保持O(1/n)衰减，真人数据比例μ需按n^(2.5+γ)（γ>0）的速率缩放，远高于过往欧氏度量推导的μ~n的乐观估计；当比例满足阈值时，模型分布会指数收敛到真人分布附近的稳定Fisher-Rao球内。
### 核心结论
高维概率空间下用合成数据迭代训练时，真人数据的需求量远高于欧氏度量给出的乐观估计，低估会直接导致模型崩塌
