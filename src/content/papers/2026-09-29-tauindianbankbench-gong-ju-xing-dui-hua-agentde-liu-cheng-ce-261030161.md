---
title: 'TauIndianBankBench: Procedure-Aware, Action-Oriented Evaluation of Tool-Using
  Conversational Agents'
title_zh: TauIndianBankBench：工具型对话Agent的流程感知动作导向评测基准
authors:
- Krishanu Adhikary
- Prashant Devadiga
affiliations:
- National Payments Corporation of India (NPCI)
arxiv_id: '2610.30161'
url: https://arxiv.org/abs/2610.30161
pdf_url: https://arxiv.org/pdf/2610.30161
published: '2026-09-29'
collected: '2026-10-29'
category: Agent
direction: Agent 工具调用合规性评测基准
tags:
- Agent Evaluation
- Tool Calling
- Policy Compliance
- Conversational Agent
- Benchmark
one_liner: 推出印度零售银行场景工具Agent评测基准，双重校验流程动作与终态解决漏判问题
practical_value: '- 工具调用型服务Agent评测可复用「终态校验+动作校验+写纯净度校验」三重框架，避免漏判只读类合规步骤缺失、误判额外操作的违规场景，适配电商客服、售后等高风险操作类Agent的效果评估

  - 业务场景任务集构造可复用四类拆分逻辑：序列依赖、边界Case、稀有工具、简单控制组，既能有效区分模型能力差异，又能快速定位Agent能力短板，适配电商多场景客服、权益操作类Agent的测试集构建

  - 业务Agent的奖励函数设计可参考该评测的打分逻辑，除最终业务结果外，把合规要求的只读类查询、禁止的额外操作纳入奖罚规则，提升Agent的业务合规性，可直接落地到电商退款、改地址等高风险操作场景'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有工具型Agent评测大多仅校验最终状态，无法检测未修改数据的合规步骤缺失问题；而银行、电商等高监管、高风险场景中，类似闭单前告知用户罚金、操作前校验用户身份这类只读步骤直接影响用户体验与合规性，单靠终态校验会高估Agent实际能力，存在业务风险。

### 方法关键点
- 构造1000个印度零售银行业务任务，分四类：序列依赖（多步工具调用）、边界Case（需识别前置条件）、稀有工具（低频操作）、控制组（简单请求），配套合成银行数据库、34个业务工具、政策知识库与模拟用户
- 提出双重校验打分逻辑：终态校验对比操作后数据库与参考流程的预期结果；动作校验要求所有参考流程的工具调用（含只读类）必须出现，同时新增写纯净度规则，出现任何未要求的写操作直接判定失败，只有两项校验都通过才计为成功
- 配套发布全量1000条base数据集、200条lite快速评测集、150条训练集+50条测试集，支持所有OpenAI兼容接口的Agent评测

### 关键实验结果
在1000条任务集上评测6款开源模型，仅做终态校验时各模型通过率会虚高6.5~12.0个百分点，流程违规中最常见的是缺失必填只读步骤、缺失必填写操作；最强模型Qwen3.8-27B的综合通过率为0.849，最弱的Gemma 4 E2B仅为0.479。

**最值得记住的一句话**：高风险业务场景的工具Agent评测，必须同时校验操作流程与最终结果，仅看终态会显著高估Agent的合规性与实际能力。
