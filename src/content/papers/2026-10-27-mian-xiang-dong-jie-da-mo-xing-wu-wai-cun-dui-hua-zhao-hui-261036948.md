---
title: Self-Keyed In-Parameter Memorization for External Memory-Free Dialogue Recall
  in Frozen Language Models
title_zh: 面向冻结大模型无外存对话召回的自键式参数内存储方法
authors:
- XinYu Piao
- Myunghoon Ryu
- Joongheon Kim
- Jong-Kook Kim
affiliations:
- Korea University, Department of Electrical and Computer Engineering
arxiv_id: '2610.36948'
url: https://arxiv.org/abs/2610.36948
pdf_url: https://arxiv.org/pdf/2610.36948
published: '2026-10-27'
collected: '2026-10-28'
category: LLM
direction: LLM参数编辑 · 无外存对话记忆
tags:
- Parameter Editing
- Dialogue Memory
- Frozen LLM
- In-Parameter Storage
- Closed-form Update
one_liner: 提出Skim方法，无需外存即可将对话历史写入冻结LLM参数，实现无缓存查询召回
practical_value: '- 电商客服Agent、对话式推荐LLM可复用该思路，将用户高频偏好（如收货地址、常购品类）写入固定层参数，无需每次调用拉取全量KV缓存或RAG检索，降低推理外存开销与延迟

  - 推荐系统用户兴趣建模可借鉴自键生成逻辑：对用户历史行为片段自生成多维度查询作为匹配key，提升不同措辞query下的兴趣召回准确率

  - 工程侧可复用逐批次重新求解参数增量而非增量累加的技巧，避免顺序编辑导致的旧记忆遗忘问题，保障参数内存储的记忆稳定性

  - 该方法对实体类信息（如商品名、品牌）的召回率达81.1%，远高于描述性长文本，适合优先落地实体类用户记忆的参数内存储场景'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM对话依赖KV缓存或RAG等外部存储，随对话长度提升内存占用、推理成本持续上涨；传统参数编辑方法需提前已知待存储内容的查询key和标准答案，无法适配对话场景下未来查询未知、无标注的约束，亟需无外存的无监督对话记忆方案。
### 方法关键点
- 提出Skim框架，三步实现参数内记忆：从对话轮次提取短文本span作为待存储value，为每个span自生成多组差异化查询作为检索key，通过封闭岭回归求解参数增量，批量写入Transformer中后段FFN层下投影矩阵
- 采用判别间隔打分筛选能唯一指向对应span的key，同时生成多种措辞变体覆盖用户未来不同问法，提升召回匹配率
- 流式场景下每次新增对话批次时，从原始权重出发重新求解全量记忆对的参数增量，而非累加增量，彻底避免顺序编辑的旧记忆遗忘问题
### 关键实验
基于LongMemEval对话记忆基准测试5款开源LLM，对比KV缓存上界、无缓存下界：32轮对话时平均召回率63.1%，最强模型Qwen3-14B达75.0%，远高于无缓存的3.1%~15.6%；流式写入召回率与批量写入完全一致，无遗忘；75%的错误来自存储阶段的span提取与选择，寻址阶段错误率为0。
### 核心结论
Transformer FFN层参数可作为固定大小的键值存储，无需外部内存即可实现对话记忆高效存取，核心瓶颈是存储阶段的有效内容提取而非召回阶段的寻址。
