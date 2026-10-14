---
title: 'LifeSearch: Benchmarking Deep Research Agents for Real-World Life and Productivity'
title_zh: LIFESEARCH：面向真实生活与生产力场景的深度研究Agent基准
authors:
- Yibo Wang
- Senjie Jin
- Yansong Ning
- Xinbing Liang
- Haotian Luo
- Jiazheng Zhang
- Yuxuan He
- Will Wu
- Clarenceai
affiliations:
- Tencent LLM Department
arxiv_id: '2610.18092'
url: https://arxiv.org/abs/2610.18092
pdf_url: https://arxiv.org/pdf/2610.18092
published: '2026-10-12'
collected: '2026-10-14'
category: Agent
direction: 深度研究Agent · 真实场景评测基准
tags:
- Deep Research Agent
- Benchmark
- LLM-as-a-Judge
- Real-world Task
- Bilingual Evaluation
one_liner: 首个面向真实生活与生产力场景的中英双语深度研究Agent评测基准，含4000+专家标注评分规则
practical_value: '- 开发电商/消费类深度研究Agent（如商品对比、竞品调研、消费决策助手）时，可针对性优化3个常见失败点：避免提前终止提问、严格校验信息时间范围、覆盖所有明确要求的细节字段，可直接提升任务成功率

  - 做Agent评测时可复用这套细粒度rubric设计方法：按任务拆解子要求、标注权重、锚定数值/时间/单位等可验证指标，避免模糊主观打分，大幅提升评测一致性

  - LLM-as-a-Judge选型可参考论文实验结论，优先选择低推理开销、0温度的Gemini 3.1 Pro，无需多轮投票即可达到84%+的人评对齐度，降低评测成本

  - 内部构建业务相关Agent评测集时，可复用其数据构建pipeline：真实用户query过滤→专家任务拆解→能力维度富集→多轮质检，保证评测任务与业务场景的相关性'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有深度研究（DR）Agent评测基准多聚焦学术任务或合成数据，缺少真实生活、职业生产力场景的覆盖，无法准确衡量Agent在电商竞品调研、消费决策、行业趋势分析等落地场景的实际能力，亟需标注规范、贴合真实需求的评测基准填补空白。
### 方法关键点
- 数据集构建：从真实用户query出发，经意图过滤、领域分类、任务改写、专家筛选4步，最终产出203个中英双语任务，覆盖公司竞品调研、金融市场分析、政策查询等7个领域
- 细粒度rubric设计：投入4500+小时专家标注，构建4014条评分规则，每条规则标注类型、必要性、优先级、权重，锚定数值、单位、时间范围等可验证指标，避免主观模糊打分
- 评测框架：对比11种LLM-as-a-Judge配置后，选定低推理开销、0温度的Gemini 3.1 Pro作为打分器，单轮打分即可达到84.25%的人评对齐度，无需多轮投票降低评测成本
### 关键实验
在统一ReAct框架下评测12款前沿DR Agent，均支持web search、web fetch、code execution工具。核心结果：1）最优的GPT-5.6 Sol仅得63.4分，所有系统得分均低于70%，仍有大幅提升空间；2）输出token数与得分正相关但不决定质量，Claude Opus 5与GLM-5.3 token数相近但得分差6.9个百分点；3）整体得分与人类偏好排序的Spearman ρ达0.89，Kendall τ达0.81，评测结果高度符合人类判断。
### 核心结论
当前前沿DR Agent在真实生活与生产力场景的任务完成率仍不足三分之二，优化证据合成能力、严格校验信息时间范围、全覆盖任务要求细节是核心提升方向。
