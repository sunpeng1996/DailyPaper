---
title: 'Ask, Don''t Equip: Question-Driven Coding Agents for Deep Kernel Optimization'
title_zh: 基于问题驱动的编码Agent实现深度CUDA Kernel优化
authors:
- Gabriele Oliaro
- Jaeseong Lee
- Zhaoyuan Su
- Sreeram Vennam
- Zhihao Jia
- Samyam Rajbhandari
affiliations:
- Snowflake AI Research
- Carnegie Mellon University
arxiv_id: '2611.03517'
url: https://arxiv.org/abs/2611.03517
pdf_url: https://arxiv.org/pdf/2611.03517
published: '2026-11-02'
collected: '2026-11-03'
category: Agent
direction: Agent编码优化 · CUDA Kernel生成
tags:
- LLM Agent
- CUDA Kernel
- FlashAttention
- Evolutionary Search
- Code Generation
one_liner: 提出问题驱动的KernelSeek Agent，无需算子特定知识即可生成性能超过FlashAttention3/4的无依赖CUDA内核
practical_value: '- 长周期优化类Agent设计可借鉴「问题注入替代工具预投喂」思路：在优化停滞、Agent宣称达到极限等决策点注入无答案的引导性问题，避免搜索陷入局部最优，ROI远高于盲目叠加工具、预加载知识库

  - 可复用「可验证目标+Stop钩子」架构：把业务目标转化为机器可校验的规则（而非自然语言要求），在Agent试图终止任务时自动校验完成度，解决Agent提前宣告完成的共性问题

  - 进化搜索类优化任务可参考「问题作为搜索方向指引」的思路：将每代进化的指令替换为待验证的假设类问题，而非具体编辑要求，既能保留搜索自由度又能避免无意义试错'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前GPU Kernel优化的LLM Agent陷入结构-自由度权衡困境：脚本式Agent优化范围受预设规则限制，开放式进化Agent需要上千次试错成本极高，两类方案都缺乏优化方向指引，额外投喂的profiler分析、文档检索等工具信息往往无法解决方向缺失的核心问题，导致优化提前停滞。

### 方法关键点
- 提出KernelSeek问题驱动架构：仅保留最小校验harness，无预设优化脚本、无预消化的上下文信息，在优化停滞、Agent宣称极限、异常收益等决策点注入引导性问题，仅给予优化方向不限制具体优化动作
- 构建可复用通用问题库：将优化过程中高频出现的引导性问题提炼为101条通用条目，仅包含待验证的假设，要求Agent通过自带工具测量得到答案，无需算子或参考实现相关的特定知识
- 兼容进化搜索框架：将进化搜索每代的优化指令替换为问题类假设，引导搜索方向同时保留进化的变异自由度，避免无意义的局部重复试错

### 关键结果
- 基准对比：和同配置下工具完备的自主进化Agent对比，后者133步后仅达到FlashAttention3（FA3）性能的0.50×就停滞，KernelSeek仅用40轮交互就达到1.13×FA3
- 落地效果：生成的无依赖Hopper架构FA3内核182个场景全正确，几何平均性能1.16×FA3；Blackwell架构FA4内核154个可运行场景全正确，几何平均性能1.46×FA4，均超过cuDNN等现有最快开源实现

### 最值得记住的一句话
对于长周期优化类Agent，稀缺资源从来都不是信息和工具，而是正确的方向指引，一个恰到好处的问题比海量的预投喂知识更有效
