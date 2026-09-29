---
title: 'Draft-KV: Learning Useful Latent Communication Between Language Models'
title_zh: Draft-KV：大语言模型间的有效隐式通信方法
authors:
- Linquan Wu
- Shichang Meng
- Tianxiang Jiang
- Haoyu Yang
- Peng Zhong
- Fengming Zhu
- Xi Peng
- Linqi Song
- Jacky Keung
- Jingyu Zhang
affiliations:
- City University of Hong Kong
- University of Science and Technology of China
- Tencent AIPD
- Huawei Theory Lab
- Hong Kong Metropolitan University
arxiv_id: '2609.34754'
url: https://arxiv.org/abs/2609.34754
pdf_url: https://arxiv.org/pdf/2609.34754
published: '2026-09-27'
collected: '2026-09-29'
category: MultiAgent
direction: 多智体协作 · LLM隐式通信
tags:
- KV cache
- latent communication
- multi-agent
- LLM collaboration
- cross-model alignment
one_liner: 提出基于模型生成草稿KV状态的轻量跨LLM隐式通信方案，解决现有方案信息利用率低问题
practical_value: '- 多Agent业务系统可直接复用Draft-KV的KV状态传递方案：相比文本传递省去编解码开销，还能保留更多中间推理信息，适配推荐场景下大模型做离线用户/商品理解、小模型做实时推理的异构模型组合需求

  - 可复用配对增益（P=匹配消息精度-错配消息精度）作为隐式通信效果的核心评估指标，避免仅看系统增益带来的虚假性能提升，快速验证模型是否真的利用了协作方传递的信息

  - 1.05M参数量的轻量桥接层+三阶段渐进式训练方案可直接迁移，无需微调LLM主干，适配业务场景下冻结通用大模型、仅训小适配器的低成本落地要求'
score: 9
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM间隐式通信方案普遍宣称可提升接收方精度，但对照实验发现：将通信消息替换为不相关问题的消息后，精度下降最多不到0.6pp，说明增益大多来自接口适配而非有效信息传递，无法复用更强发送方的能力，业务落地易出现虚假提升。
### 方法关键点
- 消息设计：发送方先为当前问题生成回答草稿，提取草稿计算过程产生的KV状态作为通信内容，而非prompt阶段的静态KV
- 桥接架构：仅训练1.05M参数量的线性投影层+门控注意力分支，将发送方KV映射到接收方侧存，两个LLM主干全程冻结，参数量比SOTA方案C2C小348倍
- 训练流程：三阶段渐进式训练，先做消息重建保证可解码，再做答案对齐，最后加错配消息伤害约束，避免接收方被错误消息误导
### 关键结果
在MMLU-Redux、ARC等5个公开数据集，以及HotpotQA等2个证据拆分数据集测试：
- 以Qwen3-8B为发送方、冻结Qwen2.5-0.5B-Instruct为接收方，MMLU-Redux精度达78.04%，比Receiver-only的37.45%提升40.59pp，比错配消息的36.40%提升41.64pp，完全解决信息利用gap
- 发送方从0.6B升到8B时，Draft-KV系统增益提升32.6pp，远高于C2C的1.4pp，增益随发送方能力线性增长
- 证据拆分场景下，Draft-KV精度超过两个模型单独表现，平均比文本传递方案高6.41pp

**最值得记住的结论**：评估隐式通信不能只看系统相对单模型的增益，配对增益（正确消息与错配消息的精度差）才是通信真正携带有效信息的核心证据。
