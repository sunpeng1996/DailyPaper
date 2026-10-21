---
title: 'When Copying Is Hard: Copy-Constrained Decoding for Exact Span Reproduction'
title_zh: 面向长文本精确片段复现的复制约束解码框架CopyGen
authors:
- Jinghui Zhang
- Lang Gao
- Zongfang Liu
- Ruihong Zeng
- Zirui Song
- Rui Yan
- Kentaro Inui
- Xiuying Chen
affiliations:
- MBZUAI
- Zhejiang University
- Westlake University
- Wuhan University
- Tohoku University
arxiv_id: '2610.28393'
url: https://arxiv.org/abs/2610.28393
pdf_url: https://arxiv.org/pdf/2610.28393
published: '2026-10-20'
collected: '2026-10-21'
category: LLM
direction: LLM 可控解码 · 精确文本复制
tags:
- Controlled Decoding
- Exact Span Copy
- LLM Inference
- Decoding Plugin
- Efficient Generation
one_liner: 为冻结LLM提供轻量解码插件，无需微调即可大幅提升长片段精确复制准确率与推理速度
practical_value: '- 电商商品参数、合规文案、资质编号生成场景可直接集成CopyGen，无需微调基座即可避免字符级错误，成本极低

  - RAG回答生成需要精确引用商品参数、售后规则、用户评价原文时，可复用其三阶段解码逻辑解决引用胡编问题，同时提升生成速度

  - 电商Agent工具调用时，可基于CopyGen的logit校准逻辑保障API密钥、订单ID、商品ID等敏感字段的精确复制，降低工具调用失败率

  - 生成式推荐输出标准化Semantic ID、活动规则文案时，可复用自适应长度提案+边界校验逻辑，平衡生成效率与准确率'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
LLM在需要精确复现上下文中的长片段场景（如API密钥、法律条款、代码片段）中，常出现中间字符错误、边界溢出问题，现有拷贝机制要么只优化语义准确率要么仅提升推理速度，均不保障字符级精确性，且缺乏针对性评测基准。

### 方法关键点
- 三阶段解码框架：1）触发阶段：计算当前输出前缀与源文本的最长匹配后缀长度，结合LM隐层状态判断是否进入复制模式；2）跨度提案阶段：在对数空间自适应预测待复制片段长度，解决长度分布偏态问题；3）提案校验阶段：逐token计算源token logit与次优token的差值，用轻量偏置头校准差值，仅输出连续通过阈值的最长有效前缀
- 训练仅优化3个轻量头（触发头、长度预测头、偏置头），完全冻结基座LLM，可无缝对接SFT、vLLM/SGLang等推理引擎

### 关键实验
在合同抽取、文献证据提取、代码解释、随机序列复制4个任务上测试，覆盖Qwen3-4B/8B、Ministral-8B三个基座：冻结模型下平均Exact Match相对提升35%，推理速度最高提升15倍；结合LoRA SFT后平均Exact Match再提升4%，速度提升14.6倍；适配vLLM/SGLang后仍保持27%的Exact Match提升，速度提升5.7倍以上，插件额外耗时仅占总耗时的2.7%。

### 核心结论
LLM的可靠精确复制能力不是训练的自然副产品，而是需要显式建模的解码控制问题
