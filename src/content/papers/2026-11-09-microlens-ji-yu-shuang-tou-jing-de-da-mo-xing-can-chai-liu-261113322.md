---
title: 'MicroLens: Read, Trace, and Rewire the Residual Stream with Two Lenses'
title_zh: MicroLens：基于双透镜的大模型残差流读取、追踪与编辑工具
authors:
- Nika Zahedi
- Fangyi Zhu
- Anna Wu
affiliations:
- Stanford University
- Independent researcher
arxiv_id: '2611.13322'
url: https://arxiv.org/abs/2611.13322
pdf_url: https://arxiv.org/pdf/2611.13322
published: '2026-11-09'
collected: '2026-11-11'
category: LLM
direction: 大模型可解释性 · 残差流观测与编辑
tags:
- Residual Stream
- Logit Lens
- Jacobian Lens
- LLM Interpretability
- Model Editing
one_liner: 提出集成logit透镜与J透镜的交互式工具，支持大模型残差流的读取、溯源与实时编辑
practical_value: '- 做LLM4Rec的prompt注入/商品知识编辑时，可选用J-lens修改上游token的残差流，比直接改输出的logit
  lens更隐蔽，不影响生成内容自然度

  - 优化电商导购Agent的多跳推理路径时，可通过该工具定位知识激活的层位置，针对性做LoRA微调，减少商品信息幻觉

  - 排查推荐系统用户意图理解LLM模块的bad case时，可通过双透镜比对信息是否被模型实际使用，快速定位信息遗漏/错用原因'
score: 7
source: arxiv-cs.HC
depth: abstract
---

### 动机
现有大模型残差流解码透镜仅能输出向量对应的语义，无法判断该信息是否被模型实际调用，缺少集观测、溯源、编辑能力为一体的分析工具。
### 方法关键点
推出交互式残差流分析工具MicroLens，在token×层的二维网格上集成两类透镜：logit透镜输出当前token的对应语义，Jacobian透镜（J-lens）输出后续token会读取的语义；支持任意单元的残差向量编辑，编辑后可实时重跑后续模型计算验证影响。
### 关键结果
1. 双透镜适配不同编辑场景：logit透镜适合修改当前token输出，J透镜适合修改后续token读取的信息；
2. 两跳知识问答中，城市token的第7层即可读取到所属州/国家信息，修改该位置信息可92~98%改变最终答案；
3. 89~92%检索类问题、39~63%多跳推理问题的正确答案早于推理输出出现在残差流中，J透镜比logit透镜早1~2层检测到该信息。
