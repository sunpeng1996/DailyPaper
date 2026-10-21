---
title: 'Adaptive Replay Refinement: Allocating Test-Time Compute Between Revision
  and Resampling'
title_zh: 自适应重放优化：推理阶段计算在修订与重采样间的分配
authors:
- Ahsan Bilal
- Muhammad Ahmed Mohsin
- Muhammad Umer
- Ayesha Mohsin
- Sarmad Bilal
- Dean F. Hougen
affiliations:
- University of Oklahoma
- Stanford University
- National University of Sciences and Technology
arxiv_id: '2610.28294'
url: https://arxiv.org/abs/2610.28294
pdf_url: https://arxiv.org/pdf/2610.28294
published: '2026-10-20'
collected: '2026-10-21'
category: LLM
direction: LLM推理优化 · 测试时计算分配
tags:
- Test-Time Compute
- Inference Optimization
- Self-Refinement
- Replay Decoding
- Majority Voting
one_liner: 免训练的自适应重放优化策略，推理时动态分配算力给修订或重采样，降延迟保精度
practical_value: '- 在生成式推荐文案生成、Agent多轮思考等高吞吐量LLM场景，可复用ARR的固定点检测逻辑，生成内容不再变化时立即停止修订，释放的算力分配给新候选生成，降延迟同时不损效果

  - 推荐理由纠错、搜索query改写校验等自修订场景，可参考replay解码方法批量验证草稿不变token，串行修订延迟最高降30%，无额外训练成本

  - 多候选聚合场景（如多召回结果排序、Agent多路径决策投票）可参考ARR的算力分配逻辑：修订净修复率高于0.25%时优先分配算力给修订，否则优先多采样提升投票准确率'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM测试时算力分配要么采用固定修订轮次，在修订收敛后浪费大量冗余算力；要么依赖自校验、学习控制器，判断信号不可靠还需要额外训练成本；同时自修订多为串行逐token生成，重复生成长段不变内容，进一步推高延迟，亟需免训练、低延迟的动态算力分配方案。

### 方法关键点
- 自适应重放优化(ARR)为完全免训练方案，通过检测确定性修订的不动点（即修订后内容与输入完全一致）判断修订是否已耗尽，自动将释放的算力分配给新的独立采样
- 重放解码机制每次并行验证最多W个草稿token，仅对不一致的后缀逐token生成，输出与普通贪心修订完全等价，大幅降低串行步数
- 算力分配策略：初始启动N个并行根样本，每个根样本修订到不动点后立即销毁，空出的算力配额生成新根样本，最终对所有根样本的答案做多数投票得到结果

### 关键实验
覆盖5个模型家族的7个模型、7个推理基准（含MATH500、GSM8K等数学推理集）测试：同等算力下在3/5数学推理基准上与多数投票基线精度持平，关键路径串行步数最高降低2.4倍；MATH500上达到84.6%精度仅需要多数投票41%的串行步数，延迟降低超50%；当修订净修复率高于0.25%时ARR表现优于纯采样，否则纯采样更优。

**最值得记住的一句话：测试时算力分配不需要提前预测答案正确性，只要检测到修订不再产生变化就将算力转移给新尝试，即可在不损失精度的前提下大幅降低延迟**
