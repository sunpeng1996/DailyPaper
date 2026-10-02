---
title: 'BiasReducer: Adaptive Bias Mitigation for Reward Models'
title_zh: BiasReducer：面向大语言模型奖励模型的自适应偏差缓解框架
authors:
- Shuang Liu
- Yongliang Miao
- Yanguang Liu
- Haoyi Xiong
- Mengnan Du
affiliations:
- Carnegie Mellon University
- The Chinese University of Hong Kong, Shenzhen
- New Jersey Institute of Technology
arxiv_id: '2609.32720'
url: https://arxiv.org/abs/2609.32720
pdf_url: https://arxiv.org/pdf/2609.32720
published: '2026-09-25'
collected: '2026-10-02'
category: Training
direction: LLM 奖励模型偏差缓解优化
tags:
- Reward Model
- RLHF
- Bias Mitigation
- Model Editing
- Sparse Autoencoder
one_liner: 仅编辑奖励模型线性头，无需全量重训的自适应偏差缓解框架，效果优于现有训练类基线
practical_value: '- 电商/内容推荐场景的RLHF排序奖励模型可复用该框架，仅修改线性奖励头即可缓解长度、格式等表层特征偏好，无需全量重训，节省算力成本

  - 多场景适配时可借鉴「通用编辑池+场景化选择」的思路，预训练好常见偏差（如文案长度、emoji使用、表述自信度）的编辑向量，新场景仅需200以内无标注样本即可选择最优编辑组合，适配成本极低

  - Agent的工具调用/回答打分模块可引入该方法，缓解奖励模型对回答格式、长度的过度偏好，提升打分准确性，避免Agent为刷分生成冗余回答

  - 可复用语义监督+SAE的属性对齐方法，快速定位奖励模型的可解释偏差维度，为业务规则迭代提供依据'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
RLHF流程中奖励模型是对齐人类偏好的核心，但现有奖励模型普遍存在表层特征偏好（如更长的回答、更自信的表述、更多格式标记），会导致奖励黑客问题，下游LLM为获得更高分数优化表层特征而非回答质量。现有方案要么需要全量重训奖励模型，消耗大量数据和算力，要么只能针对预先指定的单一偏差做固定校正，无法适配不同数据集的偏差分布差异。

### 方法关键点
- 用带语义监督的SAE式编解码器，从偏好对的隐层差异中学习长度、自信度、谄媚性等7种预定义表层属性的可解释表征维度，每个维度对应一个明确的偏差类型
- 针对每个属性计算奖励头的校正方向和强度，构建可复用的编辑池，校正过程仅修改线性奖励头的参数，不改动Transformer主体
- 针对新数据集，无需偏好标注，仅通过奖励得分与各属性的相关性、编辑对得分的影响程度两个信号排序，自动选择需要校正的偏差，支持单属性校正（BIASREDUCER-S）和多属性组合校正（BIASREDUCER-M）

### 关键结果
在5个公开奖励模型（参数从1.7B到8B）、3个偏差基准（RM-Bench-Hard、JudgeBiasBench、Arena-StyleConflict）上测试，BIASREDUCER-M在三个基准上分别平均提升8.3、18.0、6.9个百分点，优于RRM等两种训练类基线；下游GRPO训练中，使用校正后的奖励模型可在保持回答质量不变的前提下，降低冗余度和谄媚性，平均回答长度缩短13%左右。

### 核心洞见
奖励模型编辑的最优设计思路是：一次性学习可复用的偏差校正向量，再基于每个新数据集的实际偏差表现动态选择需要应用的校正，无需全量重训即可实现跨场景适配
