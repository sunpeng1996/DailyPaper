---
title: Measuring Task-Agnostic Training Data Influence Across Language Model Pretraining
title_zh: 大语言模型预训练过程中的任务无关训练数据影响力度量
authors:
- Yuto Nishida
- Hirokazu Kiyomaru
- Yusuke Oda
- Takashi Kodama
- Chaoran Liu
- Daisuke Kawahara
- Yusuke Miyao
- Max Müller-Eberstein
- Masaru Isonuma
affiliations:
- Nara Institute of Science and Technology
- NII LLMC
- Waseda University
- The University of Tokyo
- IT University of Copenhagen
arxiv_id: '2608.13515'
url: https://arxiv.org/abs/2608.13515
pdf_url: https://arxiv.org/pdf/2608.13515
published: '2026-08-13'
collected: '2026-08-14'
category: Training
direction: LLM预训练 · 数据影响力度量
tags:
- Data-Influence
- LLM-Pretraining
- Task-Agnostic
- Data-Curation
- Training-Dynamics
one_liner: 提出任务无关的预训练数据影响力度量方法，揭示预训练各阶段不同类型数据的贡献动态规律
practical_value: '- 垂直领域LLM预训练（如电商领域大模型）可参考阶段数据适配策略：早期加大通用/日常会话类数据占比，中后期提升代码/品类规则/专业领域数据配比，降低训练成本

  - 训练数据清洗/筛选可复用任务无关影响力评估框架，无需下游标注即可快速识别低贡献甚至负贡献的训练样本，减少噪声数据干扰

  - 领域SFT数据选择可借鉴核心思路：基于样本梯度与最终模型参数的对齐度评估样本贡献，替代依赖下游任务标注的评估方式，提升数据筛选效率'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有预训练数据影响力度量方法均绑定特定下游任务或验证集，无法客观反映数据对模型全预训练周期的真实贡献，且不同训练阶段的影响力评估依赖中间checkpoint的任务表现，难以跨阶段统一对比，无法为预训练数据配比优化、课程设计等实际场景提供无偏参考。

### 方法关键点
- 定义样本影响力为其梯度更新减少模型当前参数到最终预训练参数的平方L2距离的幅度，以最终模型为统一参考点，无需下游任务标注即可实现跨训练阶段的影响力对比
- 基于预训练过程中定期保存的中间checkpoint做近似计算，无需重新训练即可估算样本级影响力，适配大模型规模的分析需求
- 自动惩罚梯度方向与最终参数方向不一致的低质量/噪声样本，无需额外标注即可识别负贡献训练样本

### 关键实验
在Pythia、PolyPythia共18种模型配置（参数规模覆盖70M到12B）上验证，每个模型使用154个预训练checkpoint，核心结果：1）预训练早期文学类数据贡献更高，中后期STEM类数据贡献反超，该规律跨模型配置、初始化种子基本一致；2）checkpoint近似方法与精确值的斯皮尔曼相关系数在训练早期为0.592，中期达0.811，后期达0.947，准确性满足分析需求；3）训练后期负贡献样本占比达8%-10%，这类样本的更新方向与最终参数方向相反，会拖慢训练效率。

### 核心结论
预训练数据的贡献不是静态的，需根据训练阶段动态调整数据组成，而非全程使用固定混合比例的数据。
