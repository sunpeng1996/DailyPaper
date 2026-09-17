---
title: 'Selection Is Retrieval, Abstention Is Not: On-Device Tool Routing over 70
  Korean-English Actions'
title_zh: 端侧工具路由的选择与拒识分离方案：适配70个韩英混合动作
authors:
- Janghoon Lee
affiliations:
- Redrob
arxiv_id: '2609.18672'
url: https://arxiv.org/abs/2609.18672
pdf_url: https://arxiv.org/pdf/2609.18672
published: '2026-09-16'
collected: '2026-09-17'
category: Agent
direction: 端侧Agent工具路由架构优化
tags:
- Tool_Routing
- On_Device_Agent
- BM25
- Text_Embedding
- Low_Latency
one_liner: 提出将端侧工具路由的选择与拒识拆分，用轻量混合架构兼顾低延迟和高准确率
practical_value: '- 端侧轻量Agent可拆分工具选择与拒识模块，工具选择用字符3-gram BM25+别名扩充索引，仅17KB索引、0.14ms延迟，适合手机端购物助手、本地服务唤起等实时路由场景

  - 拒识模块优先用小参数量冻结语义编码器（如int8量化的multilingual-e5-base仅278MB），比BM25衍生特征分类器AUC提升0.109，可直接复用在电商端侧判断用户query是否匹配本地权益/服务的场景

  - 工具路由ranker可按业务特征选型：候选集<10个、词汇匹配占比>70%的场景用BM25即可，候选集更大、用户paraphrase多的场景再上语义编码器，平衡成本与效果'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
端侧AI助手的工具路由若全用LLM实现，延迟和内存成本过高（4B模型GPU延迟达1111ms）；纯检索替换方案虽然成本极低，但无法判断当前query是否无匹配工具，会强制返回top1结果导致错误调用，两类决策的成本收益不对称，此前缺乏量化的拆分评估。
### 方法关键点
- 把工具路由拆分为**选择（选哪个匹配工具）**和**拒识（是否存在匹配工具）**两个独立任务，单独评估效果与成本
- 选择模块采用字符3-gram BM25，支持别名扩充索引提升paraphrase匹配效果，无额外训练成本
- 拒识模块对比三类方案：BM25得分衍生特征训练的分类器、冻结的multilingual-e5-base、冻结的BGE-M3
- 数据集构造严格分离词汇匹配query和paraphrase query，排除lexical overlap对语义能力评估的干扰
### 关键实验
基于600条韩英混合query、70个本地工具的数据集验证：拆分架构对比纯BM25基线，错把服务端请求路由到本地工具的错误率从134/150降到12/150，端到端准确率从0.367提升到0.592；BM25选择模块在词汇匹配场景top1准确率达98.8%，候选集缩小到7个时paraphrase准确率提升到82.5%；拒识任务上e5-base的AUC达0.806，远高于BM25特征分类器的0.697；最终最优混合架构CPU延迟仅13.9ms，仅为4B LLM方案的1/80，危险率控制在6%的预设阈值内。
### 核心结论
端侧工具路由中，选择是天然的检索问题可完全用轻量方案实现，拒识才是必须投入神经组件的环节，架构决策由拒识成本决定，ranker选型由业务的词汇匹配占比、候选集规模共同决定。
