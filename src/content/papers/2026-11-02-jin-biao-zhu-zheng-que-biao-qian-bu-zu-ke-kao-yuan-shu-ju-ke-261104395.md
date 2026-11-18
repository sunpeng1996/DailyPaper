---
title: 'Correct Labels Are Not Enough: Reliable Metadata Can Silently Control Model
  Behavior'
title_zh: 仅标注正确标签不足：可靠元数据可隐性控制模型行为
authors:
- Renee Jia
- Jinzhou Wu
affiliations:
- R2M AI
- Cornell University
arxiv_id: '2611.04395'
url: https://arxiv.org/abs/2611.04395
pdf_url: https://arxiv.org/pdf/2611.04395
published: '2026-11-02'
collected: '2026-11-18'
category: Training
direction: LLM微调 · 元数据依赖鲁棒性
tags:
- Fine-tuning
- Shortcut Learning
- SFT
- DPO
- Model Robustness
one_liner: 发现即使训练标签全对，与答案高相关的元数据仍可隐性控制模型输出
practical_value: '- 业务SFT/DPO微调前，需清理训练样本中与目标高度相关的冗余元数据（如推荐/广告场景中item旁的曝光/点击标签、RM评分前缀、格式标记），避免模型学习捷径，上线后元数据变化时效果崩溃

  - 模型验收环节不能仅测常规准确率，需新增「元数据扰动」测试用例：比如将高评分标记移到负样本，观察模型是否仍输出正确结果，排查隐性依赖

  - DPO微调时可将β调至0.1以上，在不明显损失效果的前提下，降低模型对无关元数据的依赖程度，提升鲁棒性

  - 若需实现可控生成，可主动构造高可靠的元数据标记（如推荐场景的优质内容标签），快速引导模型输出符合业务要求的结果'
score: 9
source: huggingface-daily
depth: full_pdf
---

### 动机
当前LLM微调流程仅保证训练标签正确，忽略了样本附带的元数据（如RM评分、质量标签、格式标记）的影响：若元数据与正确答案高度相关，可能成为预测捷径，导致上线后元数据扰动时效果骤降，而常规无元数据的离线准确率评估完全无法发现这类问题。
### 方法关键点
- 基于Qwen3-8B、Gemma-2-9B、Llama-3.1-8B三类开源模型，用LoRA进行SFT/DPO微调
- 训练时在多选题正确选项旁固定加高值元数据标记（包括Reward/Score等业务常用词、Temperature等中性词、Florp等无意义词），错误选项加低值标记，所有训练样本标签100%正确
- 评估分三组：无元数据测准确率、元数据在正确选项测准确率、元数据移至错误选项测cue-follow率（模型选择标记选项的比例）
### 关键结果数字
- 训练时元数据100%关联正确答案的场景下，测试时将标记移至错误选项，模型cue-follow率达97%~100%，同时无元数据时准确率仍保持72%~78%，常规评估完全无法识别依赖
- 元数据与答案的关联度越高，模型依赖越强，当关联度从0.5升至1.0时，cue-follow率从不足10%升至接近100%
- DPO微调时β≤0.1也会出现明显依赖，β=0.1时的cue-follow率比β=0.05低约20pp
- 即使训练时使用无意义词作为标记，模型仍会形成依赖，仅推理时标记的语义会影响依赖强度
### 核心结论
仅靠正确的训练标签和常规离线准确率评估，完全无法排除模型对隐性元数据捷径的依赖，必须加入元数据扰动的鲁棒性测试
