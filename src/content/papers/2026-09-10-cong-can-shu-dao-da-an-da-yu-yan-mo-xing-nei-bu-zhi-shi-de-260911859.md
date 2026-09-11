---
title: 'From Parameters to Answers: How LLMs Retrieve and Use Their Internal Knowledge'
title_zh: 《从参数到答案：大语言模型内部知识的检索与使用机制》
authors:
- Wenkang Wei
- Yuan Fang
- Renhe Jiang
- Hong Cheng
- Xingtong Yu
affiliations:
- University of Science and Technology of China
- Singapore Management University
- The University of Tokyo
- The Chinese University of Hong Kong
arxiv_id: '2609.11859'
url: https://arxiv.org/abs/2609.11859
pdf_url: https://arxiv.org/pdf/2609.11859
published: '2026-09-10'
collected: '2026-09-11'
category: LLM
direction: 大语言模型 · 内部知识检索机制
tags:
- LLM
- Internal Knowledge
- Causal Intervention
- Hidden State
- Knowledge Routing
one_liner: 通过分层隐状态干预因果区分LLM知识路由与内容角色，揭示内部知识检索的分层动态过程
practical_value: '- 搭建LLM驱动的电商商品问答/知识查询Agent时，可针对业务知识关联（如商品-类目、商品-产地）定向干预模型中晚层的参数路由方向，降低知识幻觉，提升答案准确率

  - 优化RAG+LLM电商推荐问答链路时，可通过分层删除不同内容维度的隐态表示，测试各类召回知识对最终推荐话术的影响，精准筛选高价值召回内容

  - 做多意图用户Query理解时，可参考论文的分层探测方法，在不同层抽取路由、内容特征，区分用户是要切换检索类目还是查询具体商品信息，提升意图识别准确率'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有LLM知识机制研究多单独聚焦知识存储位置或召回流程，未明确区分「指引知识检索方向的路由信号」和「已召回的答案支撑内容」两类隐态角色，也未揭示二者在推理全流程的因果贡献变化，无法为定向管控LLM知识输出提供可落地的分层干预依据。
### 方法关键点
- 对Qwen-2.5-3B、Llama-3.2-3B、Gemma-3-4B三类模型的问题末尾位置隐状态做分层干预，因果分离两种路由（参数路由、隐态路由）和内容三类功能角色
- 设计三类对照任务：单国家-大洲问答验证参数路由效应、双国家选答验证隐态内容选择机制、多格式（名词/形容词/自定义编码）答案输出验证内容可迁移性
- 所有干预仅修改目标方向的隐态坐标，匹配等长高斯随机向量作为对照，排除通用隐态扰动的干扰
### 关键结果
- 路由信号早层即可被线性探测识别，但仅在中晚层产生可观测的答案影响，Qwen参数路由的有效干预窗口为28-32层
- 中晚层存在路由-内容权责交接：晚层干预路由对答案的影响下降超过70%，但干预已形成的知识内容仍会显著改变答案
- 三类模型的知识处理轨迹存在异质性：Gemma存在部分重叠的中分层路由-内容剖面，Llama在相同实验设置下无持续路由效应窗口
### 核心结论
LLM内部知识推理是先强化路由信号引导参数知识召回、再转向依赖已召回内容的渐进过程，且该分层机制存在强模型和任务特异性
