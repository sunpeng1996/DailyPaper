---
title: Who Is Sycophantic to Whom? Confident LLMs, Human Deference, and the Collapse
  of Trust Calibration
title_zh: 自信错漏大模型下的人类顺从行为与信任校准失效研究
authors:
- Deepthika S
- Pawni Yadav
- B. Sankar
affiliations:
- Amrita Vishwa Vidyapeetham
- Netaji Subhas University of Technology
- Indian Institute of Science (IISc)
arxiv_id: '2610.31579'
url: https://arxiv.org/abs/2610.31579
pdf_url: https://arxiv.org/pdf/2610.31579
published: '2026-10-22'
collected: '2026-10-24'
category: LLM
direction: LLM人机交互 · 信任校准评估
tags:
- LLM
- Trust Calibration
- Human-AI Interaction
- Sycophancy
- Misinformation
one_liner: 通过对照实验验证自信错误LLM会引发人类顺从吸收错漏信息，提出人类顺从指数量化人类侧谄媚行为
practical_value: '- 搭建电商LLM导购/客服Agent时，需增加错误回答置信度显式标记能力，避免用户吸收错误商品/活动信息引发客诉

  - 做LLM辅助的商品文案/种草内容生成审核时，不能默认人类审核者能识别高自信表述的LLM错误，需额外叠加客观事实校验环节

  - 评估LLM推荐/导购应用可靠性时，除模型侧准确率指标，还需纳入用户端错误信息吸收率作为业务指标，避免单维度评估偏差'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有LLM sycophancy研究仅关注模型迎合用户偏好的单向行为，未验证自信表述的错误LLM是否会引导用户顺从接受错漏信息，缺乏双向信任校准评估方法。
### 方法关键点
招募32名被试与基于GPT-5-mini搭建的5类助手聊天学习科学知识，助手事实错误率分别为0/25/50/75/100%且所有表述均为高置信度语气，学习后通过 surprise quiz 测试被试知识掌握情况与答案置信度。
### 关键结果
被试测验得分从满分10的7.4降至2.9，错误事实接受率达60%（正确场景仅11%，odds ratio 12.5），对错答案的置信度区分AUROC从0.7降至随机水平，用户事后对助手的信任评分无明显变化，提出baseline-corrected Human Deference Index量化人类侧顺从行为。
