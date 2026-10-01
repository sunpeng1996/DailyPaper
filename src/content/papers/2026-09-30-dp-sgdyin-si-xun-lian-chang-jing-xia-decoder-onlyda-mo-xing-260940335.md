---
title: Is Weight Tying Still Beneficial for Decoder-Only LLMs in Private Settings
  Under DP-SGD?
title_zh: DP-SGD隐私训练场景下Decoder-only大模型权重绑定效用研究
authors:
- Razan El Mais
- Ali Chehab
- Ibrahim Issa
- Razane Tajeddine
affiliations:
- American University of Beirut
arxiv_id: '2609.40335'
url: https://arxiv.org/abs/2609.40335
pdf_url: https://arxiv.org/pdf/2609.40335
published: '2026-09-30'
collected: '2026-10-01'
category: LLM
direction: LLM隐私训练 · DP-SGD优化
tags:
- DP-SGD
- Weight Tying
- Ghost Clipping
- Decoder-only LLM
- Differential Privacy
one_liner: 发现DP-SGD下解绑嵌入优于权重绑定，兼容ghost clipping降低60%以上显存
practical_value: '- 涉及用户敏感数据的LLM微调（如电商用户评论、搜索行为、个性化推荐prompt微调）时，优先选择输入输出嵌入解绑的Decoder-only模型，可在DP-SGD隐私约束下获得更高精度与训练稳定性

  - 结合ghost clipping实现低显存DP训练时，解绑嵌入的模型可直接复用官方标准ghost clipping实现，无需额外开发交叉项修正逻辑，大幅降低工程落地成本

  - 非隐私训练场景下仍可保留权重绑定的参数效率优势，无需改动原有LLM架构设计'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
DP-SGD是当前LLM隐私微调的主流方案，可提供严格的差分隐私保证，避免模型泄露训练数据中的用户敏感信息；ghost clipping是降低DP-SGD显存开销的核心技术，可将显存占用降低60%以上，但其依赖梯度块可分的假设。当前主流Decoder-only LLM普遍采用的输入输出嵌入权重绑定设计，会破坏该假设，权重绑定在隐私训练场景下的效用尚未被系统验证，急需明确最优架构选择。
### 方法关键点
- 选取GPT2（124M参）、DistilGPT2（82M参）两个典型Decoder-only架构，分别构造权重绑定（WT）、输入输出嵌入解绑（No-WT）两个对照变体，排除模型容量差异干扰
- 覆盖三种训练范式：非私有SGD、DP-SGD普通裁剪、DP-SGD ghost裁剪，全面对比效用与效率
- 推导权重绑定场景下ghost裁剪的梯度范数修正公式，明确共享参数带来的交叉项对梯度范数计算的影响
### 关键实验结果
在GLUE基准的SST-2、QNLI、QQP三个任务上测试，隐私预算ϵ=3条件下：
1. 非私有场景下WT与No-WT精度完全一致，WT可降低24%~32%的参数量
2. DP-SGD普通裁剪下，No-WT比WT精度高2.6~4.74个百分点，训练稳定性（跨seed标准差）提升1~5倍
3. No-WT结合ghost裁剪时，精度与普通裁剪完全一致，显存占用降低64%~67%
4. 权重绑定场景下引入交叉项修正可恢复精度，但训练耗时提升7~8倍，完全抵消ghost裁剪的效率优势
### 核心结论
隐私训练场景下需重新评估传统LLM架构设计的适用性，解绑嵌入+ghost裁剪是当前Decoder-only LLM DP训练的最优性价比方案
