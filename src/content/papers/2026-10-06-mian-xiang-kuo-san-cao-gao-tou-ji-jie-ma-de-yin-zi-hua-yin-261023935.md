---
title: Factorization-Guided Training and Inference for Diffusion-Drafted Speculative
  Decoding
title_zh: 面向扩散草稿投机解码的因子化引导训练与推理方法
authors:
- Jiakun Fan
- Min Xiao
- Qiang Wang
- Neiwen Ling
- Zhichao Liu
- Zhihao Jia
- Dimitrios S. Nikolopoulos
- Zijun Wei
affiliations:
- Virginia Tech
- Carnegie Mellon University
- ByteDance
arxiv_id: '2610.23935'
url: https://arxiv.org/abs/2610.23935
pdf_url: https://arxiv.org/pdf/2610.23935
published: '2026-10-06'
collected: '2026-10-20'
category: LLM
direction: LLM推理优化 · 投机解码
tags:
- Speculative Decoding
- Diffusion Drafter
- LLM Inference Acceleration
- Training Optimization
- Inference Configuration
one_liner: 通过两个因子化框架优化扩散drafter的训练与推理，实现LLM推理最高4.14倍加速
practical_value: '- 业务侧LLM服务优化：可复用训练+推理联合优化思路，在不增加推理开销的前提下提升投机解码速度，降低电商客服、商品文案生成、Agent决策等场景的LLM调用成本

  - 排序/生成类任务训练优化：可迁移位置损失因子化思路，将序列依赖约束（比如推荐排序的前缀偏好、生成文案的语序合规要求）引入损失权重设计，提升端到端业务指标

  - 推理部署调优：可复用MAT/延迟的因子化调优框架，针对不同并发、业务场景动态选择最优block size、小模型深度，平衡服务吞吐和响应延迟

  - 小扩散模型落地：如果业务用小扩散模型做短文本生成（如搜索query联想、营销短文案），可直接复用混合horizon训练+接受度加权损失的训练trick提升生成准确率'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有扩散drafter投机解码存在两个核心痛点：一是验证阶段仅接受首个错误前的连续前缀，单纯提升单token预测准确率无法有效提升平均接受token数（MAT）；二是MAT提升未必对应吞吐上涨，若单轮延迟增幅超过MAT增益反而会降低效率，现有方案未联合优化训练阶段的前缀依赖和推理阶段的MAT-延迟权衡。

### 方法关键点
- 训练侧：提出位置级损失三因子分解（是否纳入损失/权重/预测损失），设计混合horizon训练（8/16/24/32等长采样）、块内解掩码、接受度加权损失三个策略，对齐前缀接受规则提升MAT，无额外推理开销
- 推理侧：提出吞吐因子化公式G=MAT/单轮延迟，针对目标层融合深度、drafter深度、推理块大小三个维度做配置搜索，利用混合训练的特性无需重新训练即可适配不同块大小

### 关键实验
在GSM8K、HumanEval、MT-Bench等6个基准测试上，对比DFlash、EAGLE-3、PARD-2等SOTA基线，在Qwen3-4B、Qwen3-8B上分别取得3.84×、4.14×的平均AR解码加速，比SOTA基线DFlash分别提升9.1%、7.1%；推理配置搜索策略相比固定配置可额外带来最高9.75%的平均加速。

**最值得记住的一句话**：序列生成类任务的优化不能只看单token预测准确率，要结合下游验证逻辑和吞吐-延迟的工程约束做端到端联合设计
