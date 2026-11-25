---
title: 'FOL-Proof: Verifying LLM Text-to-Logic Translations via Deterministic Semantics'
title_zh: FOL-Proof：基于确定性语义的LLM自然语言转FOL翻译校验框架
authors:
- Yisrael Clark
- Guy Katz
affiliations:
- The Hebrew University of Jerusalem
arxiv_id: '2611.33078'
url: https://arxiv.org/abs/2611.33078
pdf_url: https://arxiv.org/pdf/2611.33078
published: '2026-11-24'
collected: '2026-11-25'
category: Reasoning
direction: 逻辑推理 · LLM翻译保真度校验
tags:
- First-Order Logic
- Logical Reasoning
- LLM Verification
- Semantic Analysis
- SMT Solver
one_liner: 提出无需基准真值的确定性语义校验管道，实现LLM生成FOL翻译的近完美保真度校验
practical_value: '- 电商/广告Agent涉及规则类推理（如促销权益校验、定向规则生成、用户需求转结构化查询）时，可复用「确定性语义候选池+SMT等价校验」思路替代LLM-as-judge，大幅降低逻辑错误

  - 业务中需要校验LLM生成的结构化输出（如SPARQL、促销规则AST）保真度时，可借鉴其「候选解析池+等价性校验+保守弃权」架构，避免错误规则流入下游

  - 做LLM输出自动化修复时，可复用「距离最近的合法语义候选作为矫正参考」的思路，比盲目重试的修复效果提升10倍以上

  - 高可靠推理场景（如金融风控规则生成、电商合规文案校验）可借鉴其严格门控机制，校验通过的输出准确率可达100%，适合可容忍部分弃权的场景'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
神经符号推理架构依赖LLM将自然语言转译为一阶逻辑（FOL）后交给符号求解器推理，但LLM翻译常出现量词范围错误、否定遗漏、逻辑连接词误用等问题；现有校验方法要么依赖单基准真值无法适配自然语言歧义，要么用LLM-as-judge本身存在逻辑缺陷，无法保障翻译保真度，最终导致下游推理出错。

### 方法关键点
- 基于ERG语法和MRS语义表示，从源自然语言句子确定性生成所有合法语义解析候选，覆盖量词范围、介词附着等自然语言歧义场景
- 对LLM生成的候选FOL先做合规性校验，再做谓词归一化，通过Z3 SMT求解器校验其是否与任意一个合法语义解析的FOL等价
- 采用保守策略：仅确认等价时返回「通过」，确认所有解析都不等价返回「不通过」，其余情况（解析不完整、求解超时、语法不支持）返回「弃权」，避免误判
- 支持校验后修复流程：可输出结构化错误诊断，或给出最接近的合法语义候选指导LLM重写

### 关键结果
在ProofWriter、RuleTaker、PrOntoQA三个公开基准及自建对抗基准LongFaithCheck上测试，对比LLM直接裁判、往返翻译等基线：
1. 受控单语义突变检测任务准确率100%，远高于基线最高的97.6%
2. LLM生成翻译校验任务准确率达99.7%~100%，远高于基线最高的86%
3. 作为下游推理门控时，所有通过校验的样本推理准确率100%
4. 修复环节仅给诊断信息时修复率从4.8%提升到22.8%，给出合法候选时修复率达62.6%

最值得记住的一句话：高可靠逻辑推理场景下，确定性语义分析+符号求解的校验效果远好于依赖LLM自身的校验能力
