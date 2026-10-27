---
title: 'AgentProofBench: Benchmarking Reusable Verifiers for Web Agents'
title_zh: AgentProofBench：面向Web Agent可复用验证器的基准测试集
authors:
- Jingjie Ning
- Xueqi Li
- Yi Lu
- Yibo Kong
affiliations:
- Carnegie Mellon University
arxiv_id: '2610.34634'
url: https://arxiv.org/abs/2610.34634
pdf_url: https://arxiv.org/pdf/2610.34634
published: '2026-10-24'
collected: '2026-10-27'
category: Agent
direction: Agent 可复用验证器评测基准构建
tags:
- Web-Agent
- Verifier
- Benchmark
- Reusable-Verification
- Execution-Evaluation
one_liner: 推出连接初始状态适配性与执行影响的Web Agent可复用验证器评测基准
practical_value: '- 搭建电商自动化Agent（工单处理、商品上下架审核）的验证模块时，可复用代码验证器的成本摊销阈值约10次调用，超过该次数用静态生成的验证器比每次调用LLM做判断更具性价比

  - 验证器设计必须强制从当前运行时状态读取业务绑定信息，禁止硬编码初始状态常量，避免业务规则/数据变更后出现误判

  - Agent执行失败后给出中性反馈（仅告知不通过+要求保留已完成工作继续执行）的效果优于带错误细节的反馈，基线正确交付率比程序门控高9~27个百分点

  - 验证器上线前可采用「初始状态变换+历史决策重放」的组合测试验证鲁棒性，能提前发现90%以上的规则迁移错误'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Web Agent验证器大多针对固定初始状态设计，当业务数据/规则变更、用户指令不变时，固化的验证规则容易产生误判，且缺少验证器决策对后续执行链路影响的评估能力，无法支撑可复用验证器的选型和优化。
### 方法关键点
- 覆盖97个任务、79个任务族、4类Web服务，配套版本化参考规则、可复现业务状态、执行轨迹等资源
- 设计两类核心测试：① 初始状态配对测试：固定验证器代码与用户指令，变更初始状态绑定/规则，结合全状态面板校验与历史决策重放测试验证器的状态适配能力；② 执行有效性测试：关联验证器部署状态的正确性与后续Agent执行的交付结果
- 提供统一的`verify(task, before, after)`调用接口，返回Pass/Fail/Unknown/Error四类结果
### 关键实验
测试采用DeepSeek Flash/Pro模型：① 复用验证器与重建验证器的BA差距分别为-1.56pp（95%置信区间[-5.47, 1.57]）、-4.95pp（[-10.16, 0.00]），无统计显著差异；② 部署状态面板无错误的验证器支撑的任务中，32/33的任务两次执行均正确交付，面板有错误的仅1/11正确交付；③ 中性反馈基线正确交付率比程序门控高13.6~27.3pp，验证器成本摊销阈值约10次调用。
### 核心结论
可复用验证器的鲁棒性核心是能从运行时before状态动态读取规则绑定，而非依赖构造时的硬编码常量，其部署前的状态变换测试通过率直接决定上线后的执行正确率。
