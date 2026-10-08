---
title: The Impact of Backbone Evolution on LLM-Based Relevance Assessments
title_zh: 大模型 Backbone 迭代对 LLM 相关性评估效果的影响研究
authors:
- Chuting Yu
- Guido Zuccon
- Teerapong Leelanupab
affiliations:
- The University of Queensland
arxiv_id: '2610.09820'
url: https://arxiv.org/abs/2610.09820
pdf_url: https://arxiv.org/pdf/2610.09820
published: '2026-10-07'
collected: '2026-10-08'
category: Eval
direction: LLM 评估 · 相关性判断稳定性
tags:
- LLM-as-Judge
- Relevance Assessment
- Backbone Evolution
- Prompt Stability
- IR Evaluation
one_liner: 固定prompt下同家族LLM新版本无法稳定提升相关性评估效果，且普遍存在正确判断的能力回归
practical_value: '- 做LLM驱动的相关性评估（如搜索结果判分、推荐物料审核、广告落地页校验）时，不要盲目升级同家族LLM版本，升级后必须用已标注的小批量
  golden 样本做回归验证，避免正确判分出现波动

  - 选择评估prompt框架时，若LLM版本迭代频繁优先选择结构简单的零-shot prompt（如UMBRELA）降低回归率；若面临大版本架构升级，可选择rubric类结构化prompt（如EXAM）缓冲性能下降

  - 若考虑用旧版低价LLM替代新版降本，需提前评估降级损失，研究显示降级的回归率普遍是正向升级的2-3倍，不要盲目为成本牺牲评估准确率'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
LLM 作为自动相关性判分 Judge 已广泛应用于搜索、推荐、广告领域的效果评估与物料审核，可大幅降低人工标注成本。行业普遍默认同家族新版本 LLM 是可直接替换的更优选项，固定 prompt 下效果会持续提升，但该假设缺乏实证验证，版本迭代带来的评估稳定性风险被严重低估。
### 方法关键点
- 控制变量设计：固定评估 prompt 不变，仅更换同家族不同版本 LLM backbone，覆盖 Gemini、GPT 两类商业模型和 Qwen、Llama 两类开源模型
- 测试两类主流判分框架：零-shot 结构化 prompt 框架 UMBRELA、两步 rubric 式评估框架 EXAM，EXAM 的判分 rubric 由家族最早版本生成并固定，排除 rubric 变化的干扰
- 双重评估维度：① 聚合层面与人工标注的 Exact Match (EM)、MAE、Pearson 相关系数；② 实例级回归率，即旧版正确判分的样本新版判错的比例
### 关键实验结果
基于 TREC 2019/2020 Deep Learning Track passage 排序标注数据集（0-3级 relevance 人工标签）测试：
- 无一致证据显示同家族新版本能提升判分效果，例如 GPT-4o Mini 升级到 GPT-5 Mini 时，UMBRELA 框架下 EM 从 55.8% 暴跌至 35.63%
- 即使聚合指标提升，也普遍存在 10%-30% 的实例级回归，例如 Llama3 升级到 Llama3.1 时 EM 接近翻倍，但仍有 6.7% 的旧版正确样本被新版判错
- EXAM 框架在小版本升级时回归率比 UMBRELA 高 2-3 倍，但大版本架构升级时可缓冲 20% 以上的性能下降

固定 prompt 下，同家族 LLM 新版本永远不是安全的「drop-in」替换，任何版本升级都必须做相关性判分的回归验证。
