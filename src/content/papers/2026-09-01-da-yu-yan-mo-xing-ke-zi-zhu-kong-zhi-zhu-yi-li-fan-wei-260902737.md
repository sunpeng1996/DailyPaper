---
title: Language Models Can Control Their Own Attention
title_zh: 大语言模型可自主控制注意力范围
authors:
- Namgyu Ho
- Huzama Ahmad
- Woosung Koh
- Se-Young Yun
- Tal Schuster
- Cicero Nogueira dos Santos
affiliations:
- KAIST AI
- Google DeepMind
arxiv_id: '2609.02737'
url: https://arxiv.org/abs/2609.02737
pdf_url: https://arxiv.org/pdf/2609.02737
published: '2026-09-01'
collected: '2026-09-03'
category: LLM
direction: 长上下文LLM · 推理效率优化
tags:
- Attention Optimization
- KV Cache
- Long Context LLM
- Inference Efficiency
- Zero-shot Prompting
one_liner: 提出零样本声明式注意力协议，令LLM主动声明注意力区域，大幅降低长上下文解码KV cache开销
practical_value: '- 电商/推荐Agent的长会话推理场景可直接复用DA三模式设计，将历史交互、商品库、营销规则等上下文按语义切分为magic chunk，引导LLM仅访问相关分段KV
  cache，可降低长会话推理延迟30%以上

  - 工程侧可直接参考vLLM的块对齐KV cache masking实现，无需修改注意力内核，仅通过钩子重写KV块表即可实现稀疏注意力，无缝适配现有生成式推荐、Agent服务栈

  - 生成式推荐的长上下文Item召回场景，可预将候选Item池切分为语义对齐的分段，通过DA协议让LLM自主定位候选Item所在分段，在减少全局注意力开销的同时几乎不影响召回精度'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
长上下文LLM解码时每步需扫描全部KV cache，内存访问延迟占总解码时间的70%以上，是长上下文推理的核心瓶颈。现有稀疏注意力方案要么依赖静态规则无法适配动态查询需求，精度损失大；要么每步需O(N)开销的轻量KV扫描，仍未从根本上消除冗余访问。而LLM本身已隐式掌握上下文的相关性分布，无需外部打分即可判断需要关注的区域。
### 方法关键点
- 设计声明式注意力（DA）零样本协议，将生成过程拆分为三种可解析的注意力模式：`<global>`访问全上下文用于定位相关分段，`<focus>`仅访问指定的~2K token大小的magic chunk用于信息提取，`<local>`仅访问模型自身已生成内容用于运算推理
- 上下文预先按段落、句子等语义边界切分为magic chunk，用模型原生熟悉的工具调用格式呈现，无需微调即可引导LLM输出符合语法的注意力声明标签
- 推理侧部署DA状态机，实时解析LLM输出的标签动态构造块对齐的注意力掩码，通过钩子重写vLLM的KV cache块表，无需修改内核即可兼容FlashAttention等现有加速算子
### 关键实验
在15个长上下文任务（涵盖大海捞针、多文档QA、代码库QA、对话历史问答等，上下文长度最高达1M tokens）上测试，对比基线为全注意力原生LLM、无掩码的DA prompt版本：
- Gemma-4-31B上平均降低52.0%的KV访问token数，精度仅下降1.27pp，预估解码耗时降至原生的0.71倍
- Qwen-3.6-27B上平均降低31.1%的KV访问token数，精度仅下降2.75pp，预估解码耗时降至原生的0.77倍
- 模型越大精度损失越小，上下文越长绝对节省越多，最长上下文场景下单响应最多可减少21M token的KV访问量
### 核心结论
大模型本身就知道该关注哪里，把注意力选择变成可解析的显式声明，能以极小的精度代价获得巨大的长上下文推理效率提升。
