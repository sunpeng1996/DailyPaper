---
title: Language Models that Play Chess and Explain Their Moves
title_zh: 会下国际象棋并能解释走棋逻辑的语言模型
authors:
- Adithya Bhaskar
- Jeffrey Cheng
- Danqi Chen
affiliations:
- Princeton University
arxiv_id: '2610.03695'
url: https://arxiv.org/abs/2610.03695
pdf_url: https://arxiv.org/pdf/2610.03695
published: '2026-10-01'
collected: '2026-10-05'
category: LLM
direction: 大语言模型领域专家能力融合增强
tags:
- LLM
- Knowledge Distillation
- Domain Adaptation
- Encoder-Decoder
- Reasoning
one_liner: 提出4B参数QUEEN模型，融合象棋专家编码器与指令微调LM，兼具大师级棋力与高质量走法解释能力
practical_value: '- 可复用「领域沉默专家编码器+指令微调LM+交叉注意力」架构，将推荐系统的召回/排序专家模型（如双塔召回encoder）与LLM打通，自动生成符合逻辑的商品推荐理由，解决推荐可解释性差的痛点

  - 类Bellman更新的迭代蒸馏思路可迁移到推荐/Agent场景：先让模型分析top候选决策的后续业务反馈（如推荐结果的点击率、转化率），整合生成决策解释，再蒸馏回模型，持续提升决策质量与解释一致性

  - 小参数模型通过领域知识融合超越大模型的经验可复用：电商/广告场景不需要盲目上大参数LLM，将现有成熟的领域专家模型能力与小参数指令微调LM结合，就能得到性价比更高的领域解决方案'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有领域沉默专家系统（如象棋引擎、工业级推荐排序模型）性能极强，但无法输出用户可理解的自然语言解释；大语言模型虽能生成流畅文本，但领域专业能力不足，两者能力存在明显割裂。
### 方法关键点
1. 采用交叉注意力连接的编码器-解码器架构：将领域专家编码器（象棋引擎编码器）与指令微调LM打通，通过QA课程训练让LM学会从编码器表征中抽取可解释的领域概念；
2. 提出类Bellman更新的迭代蒸馏算法：先让模型分析top候选决策的后续状态，整合生成当前决策的自然语言解释，再将解释蒸馏回模型，迭代优化决策能力与解释一致性。
### 关键结果
7轮迭代后模型Elo评分从1782提升至2697（涨幅超900），达到国际象棋大师水平，参数比前沿大模型小3个数量级，解释连贯性接近GPT-5.6-Sol（高）水平。
