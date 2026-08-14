---
title: 'DARTree: Speculative Diffusion Decoding with Autoregressive Draft Trees'
title_zh: DARTree：基于自回归草稿树的推测扩散解码加速方法
authors:
- Tianyi Li
- Yaxin Luo
- Xinyi Shang
- Zhiqiang Shen
affiliations:
- VILA Lab, MBZUAI
arxiv_id: '2608.13524'
url: https://arxiv.org/abs/2608.13524
pdf_url: https://arxiv.org/pdf/2608.13524
published: '2026-08-13'
collected: '2026-08-14'
category: LLM
direction: LLM推理加速 · 推测解码
tags:
- Speculative Decoding
- LLM Inference Acceleration
- Diffusion LLM
- Tree Construction
- Causal Correction
one_liner: 无需额外训练的树结构推测解码方法，结合因果修正大幅提升LLM无损推理速度
practical_value: '- 低并发LLM服务场景（如VIP导购Agent、个性化商品文案生成）可直接接入DARTree，无需额外训练即可获得最高9.73倍的无损推理提速，降低用户等待延迟

  - 深度批量树构建+延迟剪枝的思路可迁移到生成式推荐多候选生成场景，同深度批量打分替代逐节点串行推理，提升候选生成效率

  - 高优先级请求（如大促核心用户搜索query改写、实时推荐理由生成）可动态调整验证预算B和层宽度W，平衡 latency 与资源开销

  - 兼容现有带因果修正头的扩散草稿器（Domino、DSpark等），业务侧可基于现有推测解码组件快速改造，迁移成本低'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有扩散式推测解码存在两个核心瓶颈：单链因果修正的候选覆盖率低，容易提前出错终止；树结构构建需要逐节点串行执行AR头推理+堆操作，延迟开销大，无法同时兼顾因果依赖正确性和候选覆盖率，限制了LLM推理加速的上限。
### 方法关键点
- 无需额外训练，基于预训练的因果修正块并行草稿器，将单链因果修正扩展到树结构，同深度所有节点批量执行AR头推理，完全避免串行堆操作的延迟
- 先构建固定宽度的候选超树，所有节点打分完成后再执行全局top-B剪枝得到验证树，基于非正深度 bonus 保证前缀闭合性，大幅降低树构建 overhead
- 仅修改候选树构建逻辑，目标模型的树验证流程完全兼容现有实现，改造成本极低
### 关键结果
在7个数学、代码、聊天基准（GSM8K、HumanEval、MT-Bench等）上测试，对比DFlash、DDTree、Domino等SOTA方法：
- Qwen3-4B T=0场景下单轮最高接受12.97个token，比DFlash高98.6%、比Domino高27.9%，无损速度最高达9.73倍
- 适配DSpark等其他因果修正扩散草稿器时，接受长度最高提升40.6%，速度最高提升34.3%
> 最值得记住的一句话：低并发、延迟敏感的LLM部署场景，DARTree可在不损失生成质量的前提下，获得比现有扩散式推测解码高20%+的速度提升
