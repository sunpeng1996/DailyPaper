---
title: 'OmniDelta: Skill-Driven Budget Allocation for Token Compression in OmniLLMs'
title_zh: OmniDelta：全模态大模型技能驱动的Token压缩预算分配方法
authors:
- Haoyang Huang
- Wenjie Huang
- Tianqi Xu
- Hongyaoxing Gu
- Kang Tan
- Yikai Fu
- Yuhao Shen
- Tianyu Liu
- Baolin Zhang
- Jun Zhang
affiliations:
- 浙江大学
- 阿里巴巴通义千问应用团队
- 卡内基梅隆大学
- 中国科学院大学
- 中国科学技术大学
arxiv_id: '2607.25669'
url: https://arxiv.org/abs/2607.25669
pdf_url: https://arxiv.org/pdf/2607.25669
published: '2026-07-27'
collected: '2026-07-29'
category: LLM
direction: 全模态LLM · Token压缩推理优化
tags:
- OmniLLM
- Token Compression
- Inference Optimization
- Budget Allocation
- Training-Free
one_liner: 无训练分层预算分配框架，固定Token保留比例下提升全模态LLM压缩精度与推理效率
practical_value: '- 多模态Agent/电商内容理解场景可复用技能池路由思路：不用直接计算query与模态内容的相似度，预先构造各模态任务关键词技能池，通过query与技能池匹配度分配模态权重，准确率比直接跨模态相似度高25pp以上，无训练成本易落地。

  - 电商商品短视频/直播等多模态内容的Token压缩可复用分层预算分配逻辑：先按query意图分配音频/视频总预算，再按片段复杂度、前后帧冗余度分配帧/音频段子预算，相同压缩率下保留更多关键信息，不损失理解精度。

  - 多模态LLM推理优化可直接适配现有压缩策略：OmniDelta仅调整预算分配，与下游剪枝策略完全解耦，现有Token剪枝方案无需修改，直接插入前置预算分配模块即可提升压缩精度，7B模型可直接获得1.64倍端到端提速。'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
全模态大模型（OmniLLM）需统一处理文本、音频、视频输入，长音视频的Token序列会带来极高的内存与推理成本；现有Token压缩方法多在固定预算下筛选重要Token，忽略了前置的预算分配问题：直接用query与音视频的相似度做模态间分配不可靠，模态内均匀分配预算会遗漏关键证据、保留冗余内容，急需更合理的预算分配方案。

### 方法关键点
- 无训练分层框架，兼容现有所有Token剪枝策略，仅调整固定总保留Token的分配位置，不改变总保留比例
- 模态间预算分配：离线构造音频/视频专属技能池（各模态典型任务的关键词及语义扩展词），推理时计算query和两类技能池的嵌入相似度，按匹配度动态转移音视频预算
- 模态内预算分配：按局部单元复杂度（单元内Token多样性）、时序冗余度（和前一单元的Token相似度），给高复杂度低冗余的单元分配更多预算，低复杂度高冗余的单元压缩更激进
- 下游剪枝沿用现有规则，在分配好的单元预算内选择重要Token保留

### 关键实验
在WorldSense、AVUT、VideoMME、DailyOmni四个音视频QA基准上测试，对比全Token推理、Random剪枝、DyCoke、OmniZip等基线，基于Qwen2.5-Omni-7B/3B验证：25% Token保留率下，7B模型GPU内存降低22.0%，端到端推理提速1.64倍，各基准压缩精度均为当前最优，刷新精度-效率帕累托边界。

**最值得记住的一句话**：Token压缩的优化不止要选对留哪些Token，更要先选对把预算花在哪里，合理的前置预算分配能在无训练、不增加总保留Token的前提下，显著提升压缩性价比。
