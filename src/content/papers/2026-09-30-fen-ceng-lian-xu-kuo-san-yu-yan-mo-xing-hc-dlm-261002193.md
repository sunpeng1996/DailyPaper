---
title: Hierarchical Continuous Diffusion Language Models
title_zh: 分层连续扩散语言模型（HC-DLM）
authors:
- Hui Ren
- Zihan Li
- Chang Liu
- Huidong Liu
- Alexander Schwing
affiliations:
- University of Illinois Urbana-Champaign
- Amazon.com, Inc.
arxiv_id: '2610.02193'
url: https://arxiv.org/abs/2610.02193
pdf_url: https://arxiv.org/pdf/2610.02193
published: '2026-09-30'
collected: '2026-10-02'
category: LLM
direction: 扩散语言模型 · 离散连续耦合架构
tags:
- Diffusion Language Model
- Discrete-Continuous Coupling
- Parallel Decoding
- Flow Matching
- Text Generation
one_liner: 耦合连续隐空间扩散与离散token反馈，解决扩散语言模型并行解码的token依赖问题
practical_value: '- 生成式推荐的强约束内容生成场景（如合规商品标题、营销文案、推荐理由）可借鉴分层耦合架构，比传统离散扩散/自回归更易满足全局规则要求，减少后处理校验成本

  - 离散扩散生成模块的token依赖问题可通过「每步读token→反馈约束隐状态更新」的思路优化，解决生成内容逻辑冲突、重复、关键词遗漏等问题

  - 工程上该架构推理步数需求比同规模纯离散扩散低30%以上，适合电商实时场景如搜索query改写、个性化push文案、商品卖点生成的高吞吐要求'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
离散扩散语言模型并行解码时token独立采样，丢失依赖关系，不适合逻辑推理、全局约束类任务；纯连续扩散语言模型全程只有隐状态更新，没有离散token锚定约束，容易生成无效内容，两类方案的缺陷互补，亟需融合两者优势的统一架构。

### 方法关键点
- 构建耦合的双通路扩散过程：前向过程连续隐轨迹、离散token轨迹独立加噪，反向过程交叉约束，连续隐是唯一持久状态，每步从隐状态读取出token，再把加噪后的token作为脚手架约束下一步隐状态更新
- 推导双通路的变分下界ELBO作为训练目标，拆分为token重建损失、连续去噪损失、编码器熵正则三个可优化项，支持端到端训练
- 推理时交替执行隐状态去噪、token读取、token重加噪三步，不需要额外的解码调度策略

### 关键结果
在3类任务上均优于同参数规模基线：1. Sudoku硬集准确率72.41%，比同规模混合基线CCDD高1.68个百分点，比纯离散扩散MDM高22.53个百分点；2. Countdown CD5任务准确率37.52%，比同规模CCDD高12.17个百分点，性能追平部分85M参数的离散扩散模型；3. LM1B语言建模生成困惑度75.5，是所有扩散基线中最优，比次优的连续扩散Plaid低1.8。

### 核心结论
离散token的每步反馈既给连续隐空间去噪提供了可解释的约束锚点，又解决了并行解码的token依赖问题，是扩散语言模型兼顾生成质量和效率的可行路径。
