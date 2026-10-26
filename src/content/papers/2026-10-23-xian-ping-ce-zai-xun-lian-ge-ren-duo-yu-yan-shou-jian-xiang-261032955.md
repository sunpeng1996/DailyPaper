---
title: 'Measure Before You Train: Typed Decision Models vs. a Classical Baseline vs.
  a Generative LLM for Routing a Personal Multilingual Inbox'
title_zh: 先评测再训练：个人多语言收件箱路由的三类模型对比
authors:
- Federico Lucca
affiliations:
- Independent researcher, Trento, Italy
arxiv_id: '2610.32955'
url: https://arxiv.org/abs/2610.32955
pdf_url: https://arxiv.org/pdf/2610.32955
published: '2026-10-23'
collected: '2026-10-26'
category: Agent
direction: 个人邮件Agent决策模型评测与选型
tags:
- PersonalAgent
- EmailRouting
- TypedDecisionModel
- LLM
- Evaluation
- ModelSelection
one_liner: 对比四类邮件路由系统效果，提出个人Agent前置评测流程与选型参考
practical_value: '- 小样本（几百条标注）决策类Agent冷启动优先用TF-IDF+Logistic Regression方案，准确率普遍超过零-shot
  LLM，latency低3个数量级，成本极低

  - 不要让模型推断不属于输入文本的属性（如发件人/用户和服务方的关系），这类属性直接从已有关系图谱/标签库取，准确率可达98%+，远高于模型推理结果

  - 模型选型不要只看准确率，结合业务错误成本调阈值即可大幅降低核心损失：如调高分类器召回阈值，可将高价值消息漏判率砍半，总成本比直接用大模型更低

  - 生产Agent上线前必须做前置评测：分层采样、冻结构造输入、人工打标得到ground truth后再对比方案，避免上线后规则/模型输出完全无效都无法发现'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
个人邮件Agent的决策（分类、优先级判断、是否需要回复/生成任务/忽略）大多直接用生成式LLM或自定义规则实现，但系统自生成的标签无ground truth，错误率无法度量，很多时候无效输出都未被发现，且新型Typed Decision Model与传统方案的效果对比缺少面向个人多语言场景的实测数据。

### 方法关键点
- 提出生产Agent前置评测协议：分层采样（按预测类别平衡样本）、冻结模型输入快照、按线程分组划分数据集避免泄露、敏感信息脱敏、在Agent原生界面收集人工标注，预注册实验假设再开标注结果避免后验偏差。
- 对比9套系统：生产关键词规则、TF-IDF+Logistic Regression传统基线、4种本地/托管Typed Decision Model、3种托管生成式LLM，覆盖分类、优先级、三个Agent开关决策、发件人关系推断等任务。

### 关键结果
基于作者自用的231封意英双语真实标注邮件+500封对抗采样压力测试集，核心数据：1. 生产关键词规则分类准确率仅28%，低于58%的多数类猜题准确率，完全无效；2. 仅200条标注的Logistic Regression基线在所有字段准确率最高（类型0.79、紧急度0.74、需回复0.83、垃圾消息0.90），latency<1ms，仅无法预测极稀有类别；3. 零-shot场景下托管Typed Decision Model在开关决策上最优，Gemma 4 26B在类型分类上最优，本地Tev1 4B是端侧成本均衡选型；4. 发件人关系从联系人图谱继承准确率达98.6%，比模型从文本推断高近一倍；5. 仅看准确率Logistic Regression最优，但漏判率达18%远高于Gemma的4%，加基于错误成本的阈值后漏判率砍半，总成本低于所有LLM。

### 最值得记住的一句话
小样本决策类Agent选型核心不是模型大小，先做ground truth评测、再根据错误成本调优的传统方案，成本表现远优于直接上大模型。
