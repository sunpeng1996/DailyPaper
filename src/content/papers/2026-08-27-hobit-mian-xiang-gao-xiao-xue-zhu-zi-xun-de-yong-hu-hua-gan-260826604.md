---
title: 'hoBIT: A Profile-Aware Retrieval-Augmented Chatbot for University Academic
  Advising'
title_zh: hoBIT：面向高校学术咨询的用户画像感知检索增强聊天机器人
authors:
- Yoonseo Kim
- Seongmin Lee
- Joongheon Kim
- SeongKu Kang
affiliations:
- Korea University
arxiv_id: '2608.26604'
url: https://arxiv.org/abs/2608.26604
pdf_url: https://arxiv.org/pdf/2608.26604
published: '2026-08-27'
collected: '2026-08-28'
category: RAG
direction: 检索增强生成 · 用户画像感知优化
tags:
- RAG
- User Profiling
- Retrieval Optimization
- Chatbot
- Vertical QA
one_liner: 提出proFILL画像感知RAG框架，解决垂直领域依赖用户属性的查询应答问题
practical_value: '- 垂直领域RAG可复用离线画像标注方案：给每个文档chunk标注适用的用户属性范围（如电商场景的用户等级、地域、消费层级），检索时搭配「属性拼入query软增强+召回结果硬过滤」双策略，大幅提升召回准确率

  - 交互逻辑可复用：无需用户预先提交完整画像，先根据query识别必填属性询问，再基于首次召回结果判断是否需要补充细粒度属性二次检索，兼顾用户体验和应答准确率，适合电商客服、会员权益咨询等场景

  - 工程避坑：画像感知RAG场景不要盲目叠加通用无画像重排序器，实验证明这类重排序会破坏已匹配画像属性的召回排序，反而导致性能下降

  - 降本方案：域专属开源小模型在该框架下可达到和闭源模型相当的效果，适合私有化部署降低推理成本'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
高校学术咨询等垂直领域场景中，相同问题的答案高度依赖用户的院系、入学年份、专业类型等专属属性，传统无画像感知的RAG会召回语义相似但适用人群不符的错误文档，人工规则FAQ维护成本极高且扩展性差，亟需适配属性依赖查询的低成本RAG方案。
### 方法关键点
- 离线侧：构建画像感知索引，先将政策、通知等官方文档切分为语义chunk，用LLM给每个chunk标注适用的用户属性范围（无关属性设为null），按内容更新频率分为静态/动态双索引分开存储
- 在线侧：先做意图路由，仅检索类query进入后续流程；根据query识别所需画像属性，仅询问用户缺失的必填属性（query驱动画像）
- 召回阶段：将已获取的用户属性序列化后拼在query前做软增强，同时对召回结果做硬过滤，剔除属性不匹配的chunk；再根据召回chunk判断是否需要补充更细粒度的属性，触发二次检索（证据驱动画像）
- 交互优化：属性询问提供固定选项降低用户输入成本，所有答案附源文档链接提升可信度
### 关键实验
基于高丽大学信息学院的515份官方文档构建语料，生成1800条覆盖60种学生画像的QA实例，对比BM25、HyDE、通用重排序等基线。部署场景下proFILL的MRR达0.593，较最优基线提升432%，Source Match提升82%，Grounded Correctness达0.625；用户偏好调研中获85.3%的非平局胜率，单query平均延迟6.2秒，仅比HyDE高0.7秒。
> 最值得记住的一句话：垂直领域属性依赖的RAG场景，把用户画像匹配逻辑下沉到索引层，远好于在query或重排序层做补丁
