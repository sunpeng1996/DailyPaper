---
title: 'The Last Mile to the Real World: Agent-Native Primitives as Reusable Building
  Blocks for Solving Real-World Tasks'
title_zh: 面向真实世界任务落地最后一公里的Agent原生可复用原语框架HEELO
authors:
- Haibo Jin
- Peng Kuang
- Xiaopeng Yuan
- Lucheng Fu
- Jerry Wang
- Xucheng Yu
- Yaoning Yu
- Dehao Wu
- Runguo Li
- Colin Su
affiliations:
- University of Illinois Urbana-Champaign
- Georgia Institute of Technology
- heelo.dev
arxiv_id: '2611.07461'
url: https://arxiv.org/abs/2611.07461
pdf_url: https://arxiv.org/pdf/2611.07461
published: '2026-11-04'
collected: '2026-11-09'
category: Agent
direction: Agent架构 · 可复用原语工程
tags:
- LLM Agent
- Agent Primitive
- Harness Engineering
- Tool Use
- Real-world Task
one_liner: 提出Agent原生可复用原语及HEELO框架，显著提升20+真实世界任务完成率
practical_value: '- 可将业务通用工具、API、逻辑封装为Agent原生原语，内置小模型/规则完成参数绑定、上下文适配，降低主Agent的prompt长度与工具调用出错率

  - 业务Agent harness可参考HEELO的按需组合+证据驱动修正机制，无需构建通用固定harness，出错仅重跑牵连原语，降低运行耗时与成本

  - 电商/推荐场景的跨链路能力（如优惠核算、库存查询、订单校验）可沉淀为独立原语库，跨业务复用，避免重复开发Agent逻辑'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前LLM Agent在真实任务（工具调用、代码库维护、终端操作等）中表现不佳，核心卡在「落地最后一公里」：工具调用参数需绑定上下文、步骤间数据传递易出错、失败难以定位根因；现有方案让主Agent处理所有适配逻辑，每个任务都要重复构建能力，复用性差、成本高。

### 方法关键点
- 定义Agent原生原语：每个可复用资源（工具、代码组件、证明方法、多Agent协作模式等）自带resident LLM，封装上下文适配、参数绑定、结果校验逻辑，对外暴露自然语言接口，支持和其他原语传递消息
- 提出HEELO框架，包含三大核心机制：1）按需从原语库选择组件，组合为任务专属执行图；2）证据驱动执行，失败时仅修正被牵连的原语，其余结果保留；3）原语库独立验证迭代，仅通过领域校验（测试用例、编译通过等）的原语可入库
- 预置8类原语族，覆盖工具调用、代码开发、知识问答、多Agent协作等8类主流真实场景

### 关键结果
在20+公开基准上全场景超越基线：Terminal-Bench 4.0任务完成率从37.3%提升至55.5%，ToolBench通过率从55.8%升至75.1%，SWE-bench Verified Pass@1从73.0%升至80.5%；在真实业务平台heelo.dev的46个真实任务上，Claude Code独立完成9个，接入HEELO后完成39个，耗时降1.9倍，单任务成本降1.55倍；Codex独立完成9个，接入后完成35个，耗时降2.3倍。

**最值得记住的一句话：** 把资源的适配能力和资源本身绑定，而非交给调用方处理，是Agent规模化落地真实场景的核心思路
