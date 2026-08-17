---
title: 'Nanbeige4.2-3B on Apple Silicon: Fixing Deployment Bugs and Decreasing Looped
  Transformer Memory Overhead'
title_zh: Nanbeige4.2-3B苹果硅部署Bug修复与循环Transformer内存开销优化
authors:
- John T. Halloran
affiliations:
- University of Washington
arxiv_id: '2608.13987'
url: https://arxiv.org/abs/2608.13987
pdf_url: https://arxiv.org/pdf/2608.13987
published: '2026-08-13'
collected: '2026-08-17'
category: LLM
direction: Agent SLM部署 · Looped Transformer内存优化
tags:
- Looped Transformer
- Chunked Prefill
- MPS
- KV Cache
- Tool Calling
- Agent SLM
one_liner: 修复Nanbeige4.2-3B在苹果MPS上的部署缺陷，提出分块Prefill将上下文支持宽度提升2.7倍
practical_value: '- 部署Looped Transformer结构的Agent SLM时，可复用本文的chunked-prefill方案，在统一内存架构（如边缘设备、端侧推荐Agent）上把上下文支持长度提升2倍以上，仅损失20%-40%的吞吐量

  - 开源LLM部署踩坑时，可参考本文排查5类常见问题：RoPE buffer初始化、transformers版本API兼容、MPS端算子适配、权重序列化格式、chat
  template系统提示词冲突，大幅降低调试成本

  - 端侧Agent工具调用能力对齐时，需严格匹配SFT阶段的chat template格式（包括空格、换行符），避免自定义系统提示词覆盖原生训练模板导致的工具调用准确率下降'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
Nanbeige4.2-3B是3B参数的Agent专用小模型，基于Looped Transformer实现参数高效的深度扩展，在Agent基准上表现优于同尺寸甚至更大模型，但官方checkpoint在苹果硅MPS设备上无法开箱运行，存在稳定性、正确性问题，且Looped Transformer的层复用机制导致峰值内存翻倍，无法支撑Agent任务所需的长上下文推理，亟需适配优化。
### 方法关键点
- 定位并修复5类独立部署Bug：RoPE缓冲区零初始化、RoPE配置调度KeyError、旧版transformers缓存API不兼容、MPS专属position ID计算崩溃、权重保存键名格式错误，所有修复均采用monkeypatch不修改原生transformers包
- 提出chunked-prefill方案：将长prompt按固定chunk（默认256token）拆分处理，增量构建KV cache，将每步峰值注意力张量限制为chunk_size × 当前上下文长度，与原生Prefill输出完全一致
- 修复两类上层问题：chat template自定义系统提示词覆盖原生工具调用提示的问题，以及MPS单次OOM后永久降低可用内存的运行时问题
### 关键结果
在32GiB内存的M2 Max上测试，chunked-prefill将最大支持的上下文长度从4096提升至11231，提升2.7倍；1024token场景下批处理量提升1倍，吞吐量仅下降22.8%。修复后的模型在MCPMark easy子集任务通过率从0提升至30%，BFCL单工具调用、无需调用工具场景的准确率分别达63.3%、100%。
> 最值得记住：小参数Agent模型的落地效果50%来自训练效果，50%来自部署环节的Bug修复与内存/格式适配，创新结构落地要额外注意推理侧工程适配
