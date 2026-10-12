---
title: 'Web$hell: A Unified Interface for Agentic Web Access'
title_zh: WEB$HELL：面向LLM智能体的统一网页访问接口
authors:
- Sunghwan Kim
- Deogyong Kim
- Sangam Lee
- Donguk Kwon
- Dongha Lee
affiliations:
- Yonsei University
arxiv_id: '2610.13416'
url: https://arxiv.org/abs/2610.13416
pdf_url: https://arxiv.org/pdf/2610.13416
published: '2026-10-09'
collected: '2026-10-12'
category: Agent
direction: Agent 网页访问接口优化
tags:
- LLM Agent
- Web Access
- Unified Interface
- Agent Tooling
- Web Agent
one_liner: 统一三类网页访问模式，以更低成本提升智能体跨网页搜索、导航、深度研究任务性能
practical_value: '- 电商导购Agent可复用其信息-操作绑定设计，将商品参数、价格等信息与加购、领券等操作封装为关联对象，减少Agent切换上下文的推理成本

  - 长周期任务Agent可参考WEBCACHE架构，将访问过的页面结构化缓存并保留历史状态，支持轻量检索，大幅降低重复请求和LLM token消耗

  - 网页结构化无需依赖LLM推理，可参考WEBCOMPILER的纯HTML语义规则映射方案，稳定性高、无额外推理成本，适合业务快速落地'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有LLM智能体的网页访问模式割裂：搜索增强类适合跨页信息收集但不支持复杂交互，浏览器类适合页面操作但上下文噪声大、token成本高，文件系统类支持内容缓存但易丢失交互上下文，三类混用会导致页面重复解析，成本飙升3~6倍，无法满足长周期端到端网页任务（如电商比价、商品调研）的需求。

### 方法关键点
- 定义WEBCONTRACT统一schema，将网页内容封装为带地址、值、关联关系的信息/操作对象，直接关联信息与对应操作入口
- WEBCOMPILER基于HTML语义的纯规则，把实时DOM编译为符合WEBCONTRACT的结构化对象，无额外模型推理开销
- WEBCACHE持久化存储编译后的页面，支持多版本状态留存，提供retrieve、grep、read、execute四类统一操作，Agent无需感知底层访问模式差异

### 关键实验
在6个覆盖网页搜索、导航、深度研究的基准上对比3类主流基线：
- 性能全面领先：WideSearch F1达0.782（超最强基线+3.7%），WebArena-Verified成功率0.679（超最强基线+10.1%），DW-Bench得分31.11（超最强基线+2.74）
- 成本更低：网页导航任务平均交互轮次减少38%，token消耗降低19%，单任务成本降低8%；深度研究任务平均轮次减少43%，成本降低13%
- 鲁棒性强：缓存混入400个干扰页时，准确率无明显下降，成本仅上升4%，远低于基线的200%+涨幅

### 核心结论
智能体网页访问的核心瓶颈不是模型能力，而是接口设计的统一性，统一信息与操作的表示、减少重复解析，比单纯提升模型规格效果更好、成本更低。
