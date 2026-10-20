---
title: 'Policy Is Not Capability: Some Safety Benchmarks Measure Which Definition
  of "Unsafe" You Trained On'
title_zh: 《政策不等于能力：部分安全基准衡量训练采用的「不安全」定义》
authors:
- Vahid Jebraeeli
- Jonathon Romero
- Yijin Wang
- Adrian Chan
- Jianbang Zhang
affiliations:
- Lenovo
arxiv_id: '2610.25060'
url: https://arxiv.org/abs/2610.25060
pdf_url: https://arxiv.org/pdf/2610.25060
published: '2026-10-17'
collected: '2026-10-20'
category: Eval
direction: LLM安全评估 · 标注规则影响
tags:
- Safety-Guardrail
- LLM-Evaluation
- Benchmark-Contamination
- Label-Policy
- Knowledge-Distillation
one_liner: 通过对照实验证明LLM安全护栏基准评分更多由训练标注规则决定而非检测能力
practical_value: '- 做电商内容审核、广告合规、Agent安全护栏等分类任务时，不要盲目对标公开基准分数，优先对齐业务侧的违规定义，不同标注规则对分数的影响远大于模型架构优化

  - 需快速切换业务分类规则时，可优先采用head-only微调方案，仅更新0.03%的输出层参数即可实现全范围的分数调整，远低于全量微调成本

  - 任何模型评估前必须做训练集与测试集的精确/模糊匹配查重，本实验中over-refusal类安全基准80%以上样本出现在训练集，会严重高估模型实际效果

  - 用知识蒸馏生产小模型时，教师模型的标注规则会完全覆盖学生的硬标签规则，若业务规则变更，不能仅替换学生训练数据，需同步调整教师或新增校准层'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前LLM安全护栏的评估默认「不安全」是文本固有属性，不同模型的公开基准分数可直接横向对比，但实际业务中违规定义高度依赖场景（如版权内容在内容平台算违规、在创作工具属合法请求），现有评估体系完全忽略了标注规则对结果的干扰，导致分数无法反映真实检测能力。
### 方法关键点
- 利用工业界意外产生的双标注数据集：同一份5.3万条prompt，分别按两种规则标注：A是「moderator是否会封禁」，B是「是否为有害内容请求」，两类标注的4类一致率仅83.6%；
- 固定模型架构（ModernBERT的149M/395M两个尺寸）、代码库、优化器类型，训练10组不同标注策略的护栏模型，覆盖数据混合、知识蒸馏、head-only校准等方案；
- 对所有15个公开安全基准做去污染处理，剔除所有和训练/验证集重叠的样本后再统一评估。
### 关键结果
- 未去污染时，88%的JailbreakBench-benign、82%的OR-Bench-hard样本已出现在训练集，over-refusal类基准污染最严重；
- 固定架构下，标注规则可让HarmBench-copyright分数在0-100%全范围波动，波动幅度是规则不敏感基准（WildGuard-benign）的23倍；
- 仅微调0.03%的输出层参数，就能让基准分数跨全范围调整，且蒸馏时教师的软标签会完全覆盖学生的硬标签规则；
- 常规的标注规则A下的验证集准确率，和规则对齐度的相关系数达0.74，和真实有害内容检测能力的相关系数仅0.34。

**最值得记住的一句话**：安全护栏的基准分数更多反映你训练时采用的违规定义，而非模型的真实有害内容检测能力。
