---
title: Frontier models need only one text to unmask its human or AI author
title_zh: 前沿模型仅需单段文本即可识别作者为人类或AI
authors:
- Atrey Desai
- Deniz Böloni-Turgut
- Ty Brassington
- Minjoon Choi
- Jenna Russell
- Rishanth Rajendhran
- Bradley Emi
- Hila Gonen
- Hal Daumé
- John Wieting
affiliations:
- University of Maryland
- Simon Fraser University
- Pangram Labs
- University of British Columbia
- Google DeepMind
arxiv_id: '2611.26216'
url: https://arxiv.org/abs/2611.26216
pdf_url: https://arxiv.org/pdf/2611.26216
published: '2026-11-19'
collected: '2026-11-20'
category: LLM
direction: 大模型文本作者身份识别能力研究
tags:
- LLM
- Zero-shot
- Authorship Identification
- Text Detection
- Privacy Risk
one_liner: 零样本下用前沿大模型实现AI/人类作者、AI所属实验室、具体人类作者的多层级身份识别
practical_value: '- 可复用零样本作者识别prompt框架，用于电商UGC内容合规审核，快速定位AI生成的恶意刷单评价、水军内容

  - 可基于大模型对写作风格的匹配能力，优化个性化商品文案、营销内容生成效果，匹配用户偏好风格提升转化率

  - 风控场景可借鉴风格归因思路，识别批量异常账号的发言/评论同源性，防控黑产刷量、薅羊毛等恶意行为'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有AI文本检测工具多需训练专属模型，依赖候选集或作者写作样本，通用性差，且未覆盖多粒度作者身份识别需求。
### 方法关键点
仅输入单段文本与简单零样本prompt，无需网络访问、工具、候选列表或参考样本，调用前沿大模型实现三级身份识别：1）区分AI/人类作者；2）AI文本识别所属开发实验室；3）人类文本识别具体作者，同时可输出预测的自然语言解释。
### 关键结果数字
- Claude Fable 5.2、GPT-6.1 Sol等模型效果与专用检测工具Pangram相当
- Opus 5.5对Anthropic、OpenAI、Google生成文本的实验室识别准确率达98%
- Fable 5.2对2026年10-11月公开同行评审的作者识别准确率39%，其中Nature子样本达78%；对年发帖>500的Reddit活跃用户用户名识别准确率69%
- 识别准确率与预训练数据中作者内容曝光量、推理算力投入正相关，可通过询问模型对作者的熟悉度预判识别效果
