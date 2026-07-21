---
title: 'It''s Not What You Say, It''s How You Say It: Evaluating LLM Responses to
  Expressions of Belief'
title_zh: 表达形式优先于内容：大模型对信念表达的响应评估
authors:
- Kevin Du
- Clara Kümpel
- Michelle Wastl
- Alex Warstadt
affiliations:
- ETH Zürich
- University of Zurich
- UC San Diego
arxiv_id: '2607.18232'
url: https://arxiv.org/abs/2607.18232
pdf_url: https://arxiv.org/pdf/2607.18232
published: '2026-07-20'
collected: '2026-07-21'
category: Eval
direction: 大模型行为评估 · 信念表达影响分析
tags:
- LLM Evaluation
- Expression of Belief
- EoBench
- Context Following
- Prompt Engineering
one_liner: 提出涵盖19种信念表达类型的EoBench基准，系统性分析18款大模型的上下文依从性差异
practical_value: '- 做Agent/RAG的prompt工程时，若需要LLM优先采信上下文信息，优先使用指令式、正式语气、权威来源引用、儿童化引导这几类高说服力表达，避免使用反事实、第三方信念转述、弱确定性表述，可提升上下文注入成功率

  - 电商导购/客服Agent选型时，若需要优先采信商品库/知识库的正确信息、避免被用户错误引导，优先选择参数量更大、经过指令微调的Llama3系列模型，其上下文依从率比同规模Gemma3/Qwen3低10%-20%，抗误导性更强

  - 高风险LLM场景（比如客服改地址、退换货核验）可将用户输入的信念表达类型作为风险特征，命中高说服力EoB类型时触发二次核验，降低被恶意prompt诱导的概率'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM上下文依从性研究大多只关注内容本身，忽略了信念的语言表达形式对模型采信度的影响。而用户与LLM交互时的表达形式（语气、句式、信息来源等）差异极大，既会影响正常交互的上下文理解效果，也可能被用于误导LLM输出错误信息，目前缺乏语言学层面的系统性评估基准。

### 方法关键点
- 提出基于语言学的信念表达（EoB）分类体系，覆盖形式、证据来源、认知立场、语气4个维度共19种细粒度表达类型，包括指令式、反事实、权威引用、强弱确定性、正式/非正式语气等
- 构建EoBench基准数据集，基于PopQA事实三元组生成6.6万条可控EoB-query对，固定语义内容仅改变表达形式，与LLM参数知识形成明确冲突，隔离语言形式的影响
- 采用双向Yes/No问答方式评估上下文依从率（CFR，即模型采信上下文错误信念的比例），过滤模型本身不知道的事实样本，避免结果偏差

### 关键实验
测试18款跨架构（Llama3、Gemma3、Qwen3）、参数量1B-30B、Base/Instruct的LLM，核心结果：高说服力EoB（儿童导向语气、指令式、正式语气、权威引用）比低说服力EoB（反事实、第三方信念转述、弱认知立场）的CFR平均高30%以上；指令微调模型平均CFR比同规格Base模型低10%-15%；Llama3/Gemma3的CFR随参数量增大显著下降，30B模型比1B模型CFR低25%以上；同规模下Llama3的CFR比Gemma3、Qwen3低10%-20%，抗误导性最强。

### 核心结论
大模型是否采信上下文信息，很多时候和内容本身无关，而是由信息的表达形式决定，prompt工程和模型选型时必须考虑语言形式的影响
