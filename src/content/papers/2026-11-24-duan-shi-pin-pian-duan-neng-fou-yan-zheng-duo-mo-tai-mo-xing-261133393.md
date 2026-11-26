---
title: Can a Short Video Clip Verify a Model Fix?
title_zh: 短视频片段能否验证多模态模型的修复效果？
authors:
- Raj Shan
affiliations:
- Independent Researcher
arxiv_id: '2611.33393'
url: https://arxiv.org/abs/2611.33393
pdf_url: https://arxiv.org/pdf/2611.33393
published: '2026-11-24'
collected: '2026-11-26'
category: Eval
direction: 多模态大模型 · 版本迭代效果验证
tags:
- Multimodal LLM
- Model Debugging
- Model Evaluation
- Checkpoint Validation
- Video Understanding
one_liner: 量化短视频片段筛选多模态模型修复候选的准确率，明确其不可替代原样本终验
practical_value: '- 多模态短视频推荐/审核场景迭代模型时，可先复用错误片段做修复候选初筛，降低全量验证的算力与时间成本

  - 不可仅凭短片段测试通过就判定bug修复，必须过原样本校验，否则会产生约56%的修复误判

  - 模型版本迭代的兼容性校验可复用「错误片段初筛+原样本终验」的流程，平衡效率与准确率'
score: 7
source: arxiv-cs.MM
depth: abstract
---

### 动机
多模态视频模型迭代时，开发者常抽取能复现错误的短视频片段做快速验证，但该做法的有效性缺乏量化，无法确认是否可替代原样本完成最终校验。
### 方法关键点
在CG-Bench 960条预设视频问答任务上，从Qwen2-VL-2B-Instruct错误样本中锁定388条可复现相同错误的短片段，再用Qwen2.5-VL-7B-Instruct分别测试短片段与64帧全量原视频的结果，统计两者匹配度，补充1028条视频独立实验验证结论。
### 关键结果数字
短片段测试通过的样本中仅44%真实修复了原视频错误，仅靠片段判定修复会误判65个未修复bug；仅靠片段不通过判定未修复会漏过23.9%的真实修复；短片段仅适合做修复候选初筛，最终验证必须使用原样本。
