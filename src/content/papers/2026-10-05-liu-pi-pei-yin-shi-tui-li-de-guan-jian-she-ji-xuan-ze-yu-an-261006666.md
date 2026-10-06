---
title: What Matters for Latent Reasoning with Flow Matching
title_zh: 流匹配隐式推理的关键设计选择与FLaRe实现方案
authors:
- Yassine Ouali
- Adrian Bulat
- Georgios Tzimiropoulos
affiliations:
- Samsung AI Cambridge
- Technical University of Iasi
- Queen Mary University of London
arxiv_id: '2610.06666'
url: https://arxiv.org/abs/2610.06666
pdf_url: https://arxiv.org/pdf/2610.06666
published: '2026-10-05'
collected: '2026-10-06'
category: Reasoning
direction: 大语言模型 · 隐式推理效率优化
tags:
- Flow Matching
- Latent Reasoning
- Chain of Thought
- LLM Optimization
- Efficient Inference
one_liner: 提出5项隐式推理评估标准与FLaRe训练配方，以1/4延迟达到显式CoT 97%精度
practical_value: '- Agent推理加速场景可直接复用FLaRe思路：将高频重复的CoT推理逻辑压缩到隐空间，通过流匹配生成隐式思维替代显式token生成，可将算术类、规则类推理延迟降低75%，适合电商导购、营销活动权益计算等场景

  - 序列/语义压缩任务可复用VAE训练trick：放弃盲目追求高重建精度，通过输入token替换、隐空间加噪/dropout构造平滑隐空间，下游生成/匹配模型的效果提升更显著，可用于Semantic
  ID生成、用户长行为序列压缩

  - 低标注成本训练可复用第二阶段自训练方案：仅需query+正确答案样本，无需标注CoT，通过自生成验证通过的思维样本迭代训练，可大幅降低LLM推理能力微调的标注成本，适合电商搜索、推荐场景的用户query理解优化

  - 多路径推理场景可复用噪声采样方案：通过不同噪声采样生成多条独立推理路径，投票选最优结果，可提升复杂query解决率，适合广告文案生成、多兴趣召回的多样性优化'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
显式CoT推理延迟随链长线性增长，大量冗余描述浪费算力，现有隐式推理方法普遍存在思维贡献度低、多样性差、不可解释、无法随推理算力动态调优、效率不达预期等问题，无法满足高吞吐低延迟的业务推理需求。
### 方法关键点
- 定义有效隐式思维的5项核心评估标准：有用性、多样性、可解释性、可优化性、高效性，针对每项标准设计了对应量化探针
- 提出FLaRe两阶段训练配方：① 训练双目标VAE，将无冗余的符号CoT压缩到8×512的低维隐空间，训练时通过输入token替换、隐空间加噪/dropout构造平滑隐空间，避免高重建精度导致的生成难度上升；② 流匹配训练偏向低t（近噪声）区域，答案读取层混合噪声编码与模型自生成的隐式思维训练，适配推理时的非完美思维输入；③ 第二阶段仅用query+答案样本，基于验证通过的自生成思维做自训练，将答案损失回传到完整流生成路径
- 兼容仅含自然语言CoT的数据集：可通过LLM将自然语言CoT自动转成符号CoT后训练
### 关键结果
在GSM8K算术推理数据集上，对比Coconut、CODI、PCCoT等主流隐式推理方法，5项核心评估指标全部领先；最终效果达到显式CoT 97%的精度，推理延迟仅为显式CoT的1/4；在GSM8K-Hard、SVAMP等OOD测试集上精度也优于现有隐式推理方法。
> 最值得记住的结论：隐空间设计不要盲目追求高重建精度，平滑、信息密度高的隐编码才更适配下游生成模型
