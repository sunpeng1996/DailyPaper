---
title: Constrained Tagging for Span Labeling
title_zh: 无需训练的约束标注方法：实现跨度标注输入输出严格对齐
authors:
- Radek Štulc
- Jan Drchal
affiliations:
- Czech Technical University in Prague
arxiv_id: '2610.28922'
url: https://arxiv.org/abs/2610.28922
pdf_url: https://arxiv.org/pdf/2610.28922
published: '2026-10-20'
collected: '2026-10-22'
category: LLM
direction: LLM约束解码 · 零样本跨度标注
tags:
- Constrained Decoding
- Span Labeling
- Logits Processor
- Zero-shot Learning
- Structured Output
one_liner: 提出训练无关的约束解码标注方法，保证大模型跨度标注输出与原文完全匹配无幻觉
practical_value: '- 电商/内容平台的用户评论实体抽取、敏感内容检测、Query纠错场景可直接复用该约束解码方案，零样本下实现100% span可定位，避免普通prompting
  8.5%的span匹配失败问题，无需微调，更换标签集仅需修改prompt

  - Agent执行长文本信息抽取任务时，采用两阶段解码逻辑：推理阶段放开约束保证模型思考完整性，答案输出阶段开启约束保证输出与原文严格对齐，同时避免格式错误

  - 搜索推荐场景下的Query意图span抽取、商品标题属性抽取可采用该字节级trie+有限状态机的约束方案，支持字符级边界定位，解决重复文本的定位歧义问题'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
生成式LLM做零样本跨度标注（如NER、抽取式QA、错误检测）时存在核心痛点：输出span可能不在原文中、重复文本无法准确定位，传统BERT类方案需针对每个任务微调，标签集变更就需重训，灵活度差。
### 方法关键点
- 核心逻辑：要求LLM逐字复现输入，用自定义标记包裹目标span，通过logits处理器限制每一步输出只能是原文内容或合法标记，保证移除标记后输出与输入完全一致
- 底层实现：基于字节级token trie+有限状态机做约束校验，支持字符级span边界，哪怕边界落在token内部也可正常处理
- 推理兼容：采用两阶段解码，模型自由推理阶段不施加约束，检测到答案起始标记后再开启约束，不影响模型思考过程
- 零样本适配：无需任何训练，适配新任务仅需修改系统prompt和标签集
### 关键实验
在6个覆盖5类任务的跨度标注数据集、6个开源大模型上测试，对比无约束标注、上下文prompting、XGrammar约束JSON输出基线：
1. 255312次生成中仅0.022%失败，均为推理未关闭或token预算耗尽，无输出与原文不一致的情况
2. 普通上下文prompting有8.5%的span无法匹配到原文，该方案实现100% span可定位
3. 相同prompt下比无约束标注的F1最高提升45个点，密集标注场景（如语法纠错平均14个span/文本）下输出比JSON列表更短、推理速度更快
### 核心结论
约束解码仅能解决输出合法性与定位问题，无法优化模型选span、打标签的决策质量，后者仍需通过优化prompt或轻量微调提升
