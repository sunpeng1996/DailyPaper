---
title: 'Zuse: A Decision Model for European Languages'
title_zh: Zuse：面向27种欧洲语言的决策模型
authors:
- Umair Mehmood Imam
affiliations:
- Bineric AI
- OsloMet, Norway
arxiv_id: '2611.06238'
url: https://arxiv.org/abs/2611.06238
pdf_url: https://arxiv.org/pdf/2611.06238
published: '2026-11-03'
collected: '2026-11-18'
category: LLM
direction: 多语言大模型 · 决策任务微调
tags:
- LoRA
- Multilingual-LLM
- Decision-Model
- Calibration
- Low-Rank-Adapter
one_liner: 基于冻结开源基座加LoRA与指针头，训练3种参数量的27种欧洲语言决策模型
practical_value: '- 多语言分类/决策类业务（如跨境内容审核、工单路由）可复用「冻结基座+LoRA+指针头」的低成本微调架构，无需全量微调即可获得较好效果

  - 跨境多语言场景做模型校准调整时，优先按任务类型而非语言适配温度系数，单一温度无法覆盖所有任务的校准需求

  - 多源训练数据构建需规避两个共性坑：不同主题体系的标签词冲突、注入增强引入的捷径学习问题'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有2026年公开的决策模型均仅支持英文，无多语言（尤其是欧洲语种）的公开效果，无法满足跨境场景下分类、决策类业务需求。
### 方法关键点
基于冻结开源大模型基座，仅训练LoRA适配器与指针头，推出4B/9B/27B三种参数量的Zuse决策模型，覆盖27种欧洲语言。
### 关键结果
27B版本在11个训练外欧洲测试集（覆盖9类任务、27种语言）上准确率达87.5%，pooled预期校准误差0.016，按数据源加权为0.035。核心发现：1）校准误差由任务而非语言决定，单一温度无法同时修正知识任务过校准、可接受性判断欠校准问题；2）5%错误预算下可自动化决策占比与机会校正技能相关性（斯皮尔曼0.97）远高于原始准确率（0.91）；3）训练外语种泛化能力由基座决定，不在基座支持列表的语种效果下降23~28个点。
