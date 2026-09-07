---
title: 'Enoki: Efficient Multi-Level Hallucination Detection'
title_zh: Enoki：高效多粒度幻觉检测框架
authors:
- Elisei Rykov
- Timur Ionov
- Nikolay Ivanov
- Maksim Savkin
- Maksim Makarenko
- Alexander Panchenko
- Vasily Konovalov
- Julia Belikova
arxiv_id: '2609.00581'
url: https://arxiv.org/abs/2609.00581
pdf_url: https://arxiv.org/pdf/2609.00581
published: '2026-08-31'
collected: '2026-09-07'
category: Eval
direction: 多粒度幻觉检测 · LLM生成评估
tags:
- HallucinationDetection
- OpenIE
- MultiGranular
- FactChecking
- RAG
one_liner: 基于文本锚定OpenIE的多粒度幻觉检测框架，无需额外对齐同时输出声明级与片段级结果
practical_value: '- 电商导购/客服RAG Agent场景可直接复用ENOKI链路，实时定位生成内容中的错误商品参数、活动规则片段，无需额外做声明到文本的对齐，降低纠错开发成本

  - 线上低延迟场景可选用ENOKI-RULE或ENOKI-ENCODER版本，相比纯LLM检测方案提速2个数量级，精度损失可控，满足业务时延要求

  - 构建业务域幻觉检测数据集时，可参考ENOKIQA的双粒度标注范式，同时标注声明级事实正误和对应文本片段，兼顾可解释性输出与细粒度错误定位需求

  - 做增量式事实抽取蒸馏时，可复用匈牙利匹配的排列不变训练损失，解决多粒度抽取的行序模糊监督问题，提升小模型抽取效果'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有幻觉检测方案存在粒度割裂问题：声明级方法可给出可解释的事实校验结果，但无法定位错误对应的具体文本片段；片段级方法能精准定位错误位置，但无法输出对应的事实判断逻辑。两类方案打通需要额外的声明-片段对齐步骤，不仅推理成本高，还会引入误差传播，无法同时满足高风险业务场景下可解释性和错误定位的双重需求。
### 方法关键点
- 核心设计：以文本锚定的OpenIE关系三元组作为共享中间表示，抽取的三元组与原始文本span强绑定，无需额外对齐就能同时输出声明级验证结果和片段级定位结果
- 多后端适配：支持三类抽取模式平衡精度与效率：LLM后端（基于CycleOIE prompt扩展增量抽取规则，精度最高）、规则后端（基于依存句法的35条匹配规则，零训练、延迟最低）、编码器后端（基于ModernBERT的IGL架构，用匈牙利匹配的排列不变损失解决增量抽取的监督噪声问题，性价比最优）
- 长上下文适配：验证阶段对超长参考上下文做带重叠的分块，取所有块的最高entailment得分作为三元组的验证结果，支持长文档场景的事实校验
- 配套数据集：发布ENOKIQA双粒度数据集，包含3990条标注样本、19594条无标注样本，平均回答长度5682字符、上下文长度14879字符，同时对齐声明级和片段级标注
### 关键实验
在7个公开基准上测试，核心结果：
1. 实体级检测（HalluEntity数据集）：ENOKI-LLM AUPRC达55.09，超SOTA基线+15.3
2. 片段级定位（MuSHROOM数据集）：ENOKI-LLM Span Coverage F1达52.07，超SOTA基线+8.0
3. 效率表现：ENOKI-ENCODER比同类基线快4-10倍，ENOKI-RULE比LLM级方案提速2个数量级，精度损失在可接受范围内
### 核心结论
文本锚定的结构化事实表示，是同时实现幻觉检测可解释性和细粒度定位的低成本路径，不必在两类输出之间做二选一的架构取舍
