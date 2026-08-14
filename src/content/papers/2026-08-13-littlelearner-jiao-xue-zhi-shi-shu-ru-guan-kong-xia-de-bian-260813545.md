---
title: 'LittleLearner: Language Models Under Pedagogically Controlled Knowledge Exposure'
title_zh: LittleLearner：教学知识输入管控下的边界可控语言模型
authors:
- Fanfei Li
- Jana Zeller
- Manuel Prada-Corral
- Thaddäus Wiedemer
- Prasanna Mayilvahanan
- Ryan Cotterell
- Wieland Brendel
affiliations:
- MPI-IS
- Ellis Institute
- ETHZ
arxiv_id: '2608.13545'
url: https://arxiv.org/abs/2608.13545
pdf_url: https://arxiv.org/pdf/2608.13545
published: '2026-08-13'
collected: '2026-08-14'
category: LLM
direction: 可控边界LLM 预训练语料构建
tags:
- LLM-Pretraining
- Controlled-Knowledge
- Curriculum-Learning
- Knowledge-Boundary
- Sandbox
one_liner: 构建仅含美国K-5小学知识的88B token语料与5B参数LLM，提供知识边界可解释的模型研究沙箱
practical_value: '- 垂直领域小参数LLM研发可参考其多层过滤（预过滤+分类+符号过滤+频率采样）的语料清洗流程，精准控制模型知识边界，降低无关信息干扰

  - 搭建电商客服、商品文案生成等场景的Agent专属轻量LLM底座时，可参考限定知识范围的预训练思路，显著降低幻觉

  - 评估RAG、post-training等增量知识注入方案效果时，可复用该可控边界沙箱作为基准环境，排除预训练知识泄露干扰，测试结果更精准'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有LLM基于异构大规模web语料训练，知识边界模糊，预训练知识暴露情况难以追溯，无法精准开展知识获取、增量注入等方向的受控研究。
### 方法关键点
1. 构建LITTLECURRICULUM语料：经多层处理从FineWeb-Edu筛选得到88B token仅包含美国K-5小学阶段知识的预训练数据，严格排除5年级以上概念、事实与词汇；
2. 从零训练5B参数LLM得到LittleLearner，其能力边界完全匹配可解释的K-5教学大纲；
3. 开放语料与模型作为受控研究沙箱，测试post-training、in-context learning的知识注入效果。
### 关键结果
实验证明post-training与ICL仅能提升LittleLearner对已有知识的利用效率，无法突破预设的K-5知识边界，该沙箱可支撑缩放定律、课程学习等多方向受控研究。
