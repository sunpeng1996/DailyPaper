---
title: 'How AI Coders Discuss, Disagree, and Reach Consensus: Challenges and Opportunities
  for LLM-Based Qualitative Coding'
title_zh: 多Agent LLM质性编码的协作机制、影响因素与设计建议
authors:
- Jeongyeon Kim
- John Mitchell
affiliations:
- Stanford University
arxiv_id: '2609.11109'
url: https://arxiv.org/abs/2609.11109
pdf_url: https://arxiv.org/pdf/2609.11109
published: '2026-09-10'
collected: '2026-09-11'
category: MultiAgent
direction: 多Agent协作 自动化标注性能优化
tags:
- Multi-Agent
- Qualitative Coding
- LLM Collaboration
- Content Labeling
- Agent Debate
one_liner: 提出多Agent LLM质性编码基线流程，量化性能影响因子并给出可落地系统设计建议
practical_value: '- 多Agent标注流程可直接复用在电商商品内容打标、用户评论情感分类、广告素材合规审核等场景：先让两个Agent独立标注，再对分歧样本辩论沉淀边界规则，可大幅降低人工标注成本，提升模糊样本标注准确率

  - 标注系统优化可直接复用论文量化结论：简化标签体系定义长度、对齐标签术语与待标注内容的专业度、缩短待标注文本片段长度，无需调试prompt即可直接提升LLM标注准确率

  - Agent辩论优化技巧：无需给LLM Agent设置妥协、协作类的友好persona，鼓励多轮刚性分歧辩论而非快速共识，能挖掘更多边界样本的判断规则，进一步提升整体标注准确率

  - 可将标注过程中的Agent分歧度、Undecidable标签占比作为无监督评估信号，无需人工校验就能快速定位低质量标注批次，降低质检成本'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
当前LLM自动化质性编码研究多局限于特定领域数据集，缺乏对不同任务、数据特征下性能影响因子的系统性量化分析，开发者优化只能依赖无指导的试错，同时用户对系统透明度、可解释性的核心需求也未被充分满足。
### 方法关键点
- 基于118篇文献综述提炼4项自动化质性编码系统设计目标：输出可解释、标注不确定性可感知、准确率预期可校准、数据特征对性能的影响可解释
- 搭建多Agent基线编码pipeline：2个GPT-4o-mini Agent先独立标注，对分歧样本开展最多3轮辩论，共识后沉淀通用标注规则，再用规则重新全量编码
- 采用混合效应模型量化4类核心因子对编码准确率的影响：数据集特征、标注不确定性、Agent共识水平、辩论争议程度
### 关键结果
在教育、法律、社会学、医学4个领域的公开质性数据集上测试，Agent初始标注的Cohen's Kappa超0.85，整体F1均值0.68（区间0.31~0.89）；核心量化结论包括：代码本长度每降低1单位，初始准确率提升0.287；辩论轮次每提升1单位，最终准确率提升0.168；未达成共识的冲突越多，最终准确率越高。
### 核心记忆点
对无情感约束的LLM多Agent协作任务，刚性分歧辩论的过程价值远高于快速达成共识的结果价值
